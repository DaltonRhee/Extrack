# Contributing to Extrack

Thank you for your interest in contributing to Extrack!

Extrack is an open-source personal finance and expense tracking project. Contributions, suggestions, bug reports, and improvements are welcome.

## Getting Started

Before contributing, make sure you have:

* Python 3 installed
* Git installed
* A GitHub account
* A code editor such as VS Code

### 1. Fork the Repository

Fork the Extrack repository to your own GitHub account.

### 2. Clone the Repository

Clone your fork:

```bash
git clone https://github.com/YOUR-USERNAME/Extrack.git
```

Move into the project folder:

```bash
cd Extrack
```

### 3. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

Make sure the application works correctly before making changes.

---

## Making Changes

Before working on a large feature, consider creating or discussing a GitHub Issue first.

When making changes:

1. Keep the change focused.
2. Follow the existing project structure.
3. Keep the code easy to understand.
4. Test your changes before submitting them.
5. Update the documentation when necessary.

---

## Commit Messages

Please use clear commit messages that describe what was changed.

Good examples:

```text
Add expense category filtering
Fix dashboard calculation
Improve mobile expense table
Add transaction validation
Update installation instructions
```

Avoid unclear messages such as:

```text
update
changes
fix
stuff
final
```

---

## Pull Requests

When submitting a Pull Request, please include:

* A short description of the changes
* The related GitHub Issue, if applicable
* Information about how the changes were tested
* Screenshots when the change affects the user interface

Example:

```text
## What changed?

Added filtering by expense category.

## How was it tested?

Tested the filter with multiple expense categories
and confirmed that the displayed transactions update correctly.

## Related Issue

Closes #2
```

---

## Bug Reports

If you find a bug, please create a GitHub Issue.

Include:

* What happened
* What you expected to happen
* Steps to reproduce the problem
* Error messages, if available
* Screenshots, if useful
* Python and operating system versions

---

## Feature Requests

Feature ideas are welcome.

When requesting a feature, explain:

* What the feature should do
* Why it would be useful
* How you think it could improve Extrack

---

## Code Style

Try to keep the code:

* Simple
* Readable
* Consistent with the existing project
* Properly organized
* Easy for other contributors to understand

Avoid unnecessary changes to unrelated parts of the project.

---

## Questions and Discussions

If you are unsure about something, feel free to open a GitHub Issue or Discussion.

Constructive feedback and suggestions are welcome.

---

## Thank You

Every contribution helps improve Extrack.

Thank you for taking the time to contribute!
