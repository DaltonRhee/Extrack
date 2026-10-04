# Extrack

### Simple Personal Finance & Expense Tracker

Extrack is an open-source personal finance management application designed to make it easier to **track expenses, manage budgets, and understand spending habits** in one place.

The goal of Extrack is to provide a simple and practical way for users to keep track of their everyday finances without making financial management complicated.

> 🚧 **Project Status:** Active Development

---

## ✨ Features

* 💰 **Expense Tracking**

  * Record and manage personal expenses
  * Organize spending information
  * Keep a history of transactions

* 📊 **Financial Overview**

  * View spending information in an easy-to-understand dashboard
  * Review financial summaries
  * Understand where your money is going

* 🎯 **Budget Management**

  * Set and manage spending budgets
  * Monitor expenses against planned budgets

* 🖥️ **Simple Web Interface**

  * Clean and straightforward interface
  * Designed with usability in mind

* 🗄️ **Local Database**

  * Uses SQLite for storing application data
  * SQLAlchemy provides database interaction

---

## 🛠️ Tech Stack

| Technology     | Purpose                   |
| -------------- | ------------------------- |
| **Python**     | Main programming language |
| **Flask**      | Web application framework |
| **SQLAlchemy** | Database management / ORM |
| **SQLite**     | Local database            |
| **HTML**       | Web page structure        |
| **CSS**        | User interface styling    |
| **JavaScript** | Client-side interactions  |

---

## 📂 Project Structure

```text
Extrack/
│
├── app.py
├── models.py
├── routes.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── ...
│
└── utils/
    └── ...
```

### Main Files

**`app.py`**
Initializes the Flask application and database configuration.

**`models.py`**
Contains the database models used by Extrack.

**`routes.py`**
Contains the application's routes and request handling.

**`templates/`**
Contains the HTML templates used by the application.

**`static/`**
Contains CSS, JavaScript, and other frontend resources.

**`utils/`**
Contains helper functions used throughout the application.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DaltonRhee/Extrack.git
```

### 2. Open the project

```bash
cd Extrack
```

### 3. Create a
