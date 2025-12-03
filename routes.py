from flask import render_template, request, redirect, url_for, flash
from app import app, db
import json
# Import the Expense model and the formatting function
from models import Expense, format_large_number


# This function makes the format_large_number function available in all templates
@app.context_processor
def utility_processor():
    return dict(format_large_number=format_large_number)


# =========================
# ROUTE: Dashboard (The NEW Landing Page)
# =========================
@app.route('/')
@app.route('/dashboard') # Also keeping this for any old links
def dashboard():
    stats = Expense.get_dashboard_stats()

    # Ensure chart lists exist
    stats.setdefault('category_labels', [])
    stats.setdefault('category_values', [])
    stats.setdefault('payment_labels', [])
    stats.setdefault('payment_values', [])

    # Convert lists to JSON strings for JS
    stats['category_labels_json'] = json.dumps(stats['category_labels'])
    stats['category_values_json'] = json.dumps(stats['category_values'])
    stats['payment_labels_json'] = json.dumps(stats['payment_labels'])
    stats['payment_values_json'] = json.dumps(stats['payment_values'])

    return render_template('dashboard.html', **stats)


# =========================
# ROUTE: Show the "Add Expense" Form Page
# =========================
@app.route('/add')
def add_expense_page():
    return render_template('expense_form.html')


# =========================
# ROUTE: Handle the "Add Expense" Form Submission
# =========================
@app.route('/submit_expense', methods=['POST'])
def submit_expense():
    expense = Expense.create(
        description=request.form.get('description', ''),
        amount=request.form.get('amount', '0'),
        payment_method=request.form.get('payment_method', ''),
        categories=request.form.get('categories', ''),
        date_str=request.form.get('date', '')
    )
    if not expense:
        flash("Invalid input. Please fill all required fields correctly.", "error")
        # On error, redirect back to the form page
        return redirect(url_for('add_expense_page'))

    db.session.add(expense)
    db.session.commit()
    flash("Expense added successfully!", "success")
    # On success, redirect to the main dashboard
    return redirect(url_for('dashboard'))


# =========================
# ROUTE: Delete Expense
# =========================
@app.route('/delete/<int:id>')
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash("Expense deleted successfully!", "success")
    return redirect(url_for('dashboard'))


# =========================
# ROUTE: Edit Expense
# =========================
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    if request.method == 'POST':
        expense.update_from_form(request.form)
        db.session.commit()
        flash("Expense updated successfully!", "success")
        return redirect(url_for('dashboard'))
    return render_template('edit.html', expense=expense)