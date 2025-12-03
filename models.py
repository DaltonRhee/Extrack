import pandas as pd
from datetime import datetime, timedelta
from app import db
import numpy as np
import math

# This helper function is correct and does not need changes.
def format_large_number(num):
    """
    Formats a large number. Shows full number with commas below 1 million.
    Uses suffixes (M, B, T...) for numbers 1 million and above.
    """
    if not isinstance(num, (int, float)):
        return num 

    num = float(num)

    # FIX: Change the threshold to 1,000,000. Numbers below this will show in full.
    if abs(num) < 1000000:
        return f"₱{num:,.2f}"

    suffixes = ['', 'K', 'M', 'B', 'T', 'Q', 'E', 'Z', 'Y', 'R', 'Q']
    magnitude = int(math.floor(math.log(abs(num), 1000)))
    
    if magnitude >= len(suffixes):
        magnitude = len(suffixes) - 1
        
    value = num / (1000**magnitude)
    
    # Smart formatting for abbreviated numbers
    if value == int(value):
        formatted_num = f"{int(value)}"
    elif abs(value) >= 10:
        formatted_num = f"{value:.1f}"
    else:
        formatted_num = f"{value:.2f}"
    
    return f"₱{formatted_num}{suffixes[magnitude]}"


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(100), nullable=False)
    categories = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Expense {self.id} - {self.description}>'

    @classmethod
    def create(cls, description, amount, payment_method, categories, date_str):
        if not description or not categories or not payment_method or not date_str or not amount:
            return None
        try:
            expense_date = datetime.strptime(date_str, '%Y-%m-%d')
            amount_float = float(amount)
        except (ValueError, TypeError):
            return None
        return cls(description=description.strip(), amount=amount_float, payment_method=payment_method.strip(),
                   categories=categories.strip(), date=expense_date)

    def update_from_form(self, form):
        self.categories = form.get('categories', self.categories).strip()
        self.description = form.get('description', self.description).strip()
        try:
            self.amount = float(form.get('amount', self.amount))
        except (ValueError, TypeError):
            pass
        self.payment_method = form.get('payment_method', self.payment_method).strip()
        date_str = form.get('date', '').strip()
        if date_str:
            try:
                self.date = datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                pass

    @classmethod
    def get_dashboard_stats(cls):
        expenses = cls.query.order_by(cls.date.desc()).all()

        default_stats = {
            "expenses": [], "total_expenses": 0.0, "num_categories": 0, "longest_streak": 0,
            "avg_daily_expense": 0.0, "total_today_expenses": 0.0, "total_this_week_expenses": 0.0,
            "total_this_month_expenses": 0.0, "total_this_year_expenses": 0.0,
            "avg_expense_per_day": 0.0, "avg_expense_per_week": "tallying",
            "avg_expense_per_month": "tallying", "avg_expense_per_year": "tallying",
            "category_labels": [], "category_values": [], "payment_labels": [], "payment_values": []
        }

        if not expenses:
            return default_stats

        data = [{'date': e.date, 'amount': e.amount, 'category': e.categories, 'payment': e.payment_method}
                for e in expenses if e.date is not None]

        df = pd.DataFrame(data)
        if df.empty:
            return default_stats

        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df.dropna(subset=['date'], inplace=True)
        if df.empty:
            return default_stats
            
        df['day'] = df['date'].dt.date

        total_expenses = float(df['amount'].sum())
        num_categories = int(df['category'].nunique())

        unique_days = sorted(df['day'].unique())
        longest_streak = 0
        if unique_days:
            longest_streak = 1
            current_streak = 1
            for i in range(1, len(unique_days)):
                if (unique_days[i] - unique_days[i-1]).days == 1:
                    current_streak += 1
                else:
                    current_streak = 1
                if current_streak > longest_streak:
                    longest_streak = current_streak

        avg_daily_expense = float(df.groupby('day')['amount'].sum().mean() or 0)

        today = datetime.now().date()
        
        this_week_start = today - timedelta(days=today.weekday())
        this_week_end = this_week_start + timedelta(days=6)

        this_month_start = today.replace(day=1)
        next_month_start = (this_month_start.replace(day=28) + timedelta(days=4)).replace(day=1)
        this_month_end = next_month_start - timedelta(days=1)

        this_year_start = today.replace(month=1, day=1)
        this_year_end = today.replace(month=12, day=31)

        total_today_expenses = float(df[df['day'] == today]['amount'].sum() or 0)

        week_mask = (df['date'].dt.date >= this_week_start) & (df['date'].dt.date <= this_week_end)
        total_this_week_expenses = float(df.loc[week_mask, 'amount'].sum() or 0)

        month_mask = (df['date'].dt.date >= this_month_start) & (df['date'].dt.date <= this_month_end)
        total_this_month_expenses = float(df.loc[month_mask, 'amount'].sum() or 0)

        year_mask = (df['date'].dt.date >= this_year_start) & (df['date'].dt.date <= this_year_end)
        total_this_year_expenses = float(df.loc[year_mask, 'amount'].sum() or 0)


        avg_expense_per_day = 0
        avg_expense_per_week = "tallying"
        avg_expense_per_month = "tallying"
        avg_expense_per_year = "tallying"

        if not df.empty:
            first_day = df['day'].min()
            last_day = df['day'].max()
            num_days_spanned = (last_day - first_day).days + 1

            if num_days_spanned > 0:
                avg_expense_per_day = total_expenses / num_days_spanned
                if num_days_spanned >= 7:
                    avg_expense_per_week = avg_expense_per_day * 7
                if num_days_spanned >= 30:
                    avg_expense_per_month = avg_expense_per_day * 30.4375
                if num_days_spanned >= 365:
                    avg_expense_per_year = avg_expense_per_day * 365.25

        category_totals = df.groupby('category')['amount'].sum().to_dict()
        payment_totals = df.groupby('payment')['amount'].sum().to_dict()

        return {
            "expenses": expenses,
            "total_expenses": total_expenses,
            "num_categories": num_categories,
            "longest_streak": longest_streak,
            "avg_daily_expense": avg_daily_expense,
            "total_today_expenses": total_today_expenses,
            "total_this_week_expenses": total_this_week_expenses,
            "total_this_month_expenses": total_this_month_expenses,
            "total_this_year_expenses": total_this_year_expenses,
            "avg_expense_per_day": avg_expense_per_day,
            "avg_expense_per_week": avg_expense_per_week,
            "avg_expense_per_month": avg_expense_per_month,
            "avg_expense_per_year": avg_expense_per_year,
            "category_labels": list(category_totals.keys()),
            "category_values": list(category_totals.values()),
            "payment_labels": list(payment_totals.keys()),
            "payment_values": list(payment_totals.values())
        }