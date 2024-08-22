# Home Budget Tracker

## Overview

The Home Budget Tracker is a web application built using Flask that allows users to manage their household budget. Users can add, edit, and delete transactions, and view a summary of their income and expenses. The application also supports multiple currencies, converting amounts to PLN using exchange rates from the NBP (National Bank of Poland) API.

## Features

- Add, edit, and delete transactions
- Track income and expenses
- View a summary of the budget with balance calculation
- Visualize income and expenses with a line chart
- Convert amounts between currencies using real-time exchange rates

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tadprz123/Home_expenses
    cd Home_expenses
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000
    ```

## File Structure

- `app.py`: Main application file containing the Flask routes and logic.
- `models.py`: Defines the `Transaction` class and functions for loading and saving transactions.
- `forms.py`: Contains the `TransactionForm` class for handling form inputs.
- `templates/`: Directory containing HTML templates.
  - `base.html`: Base template for other HTML files.
  - `add_transaction.html`: Template for adding a new transaction.
  - `edit_transaction.html`: Template for editing an existing transaction.
  - `delete_transaction.html`: Template for deleting a transaction.
  - `view_budget.html`: Template for viewing the budget summary.
  - `chart.html`: Template for displaying the chart of transactions.
- `static/`: Directory for static files like CSS.
  - `style.css`: CSS file for styling the application.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: This file.

## Requirements

blinker==1.8.2
click==8.1.7
colorama==0.4.6
contourpy==1.2.1
cycler==0.12.1
Flask==3.0.3
Flask-WTF==1.2.1
fonttools==4.53.1
itsdangerous==2.2.0
Jinja2==3.1.4
kiwisolver==1.4.5
MarkupSafe==2.1.5
matplotlib==3.9.2
numpy==2.1.0
packaging==24.1
pillow==10.4.0
pyparsing==3.1.2
python-dateutil==2.9.0.post0
six==1.16.0
Werkzeug==3.0.4
WTForms==3.1.2

You can install all the requirements using:

```bash
pip install -r requirements.txt
```

## Acknowledgments

Flask - Web framework
WTForms - Forms handling
Matplotlib - Plotting library
Requests - HTTP library
NBP API - Exchange rates

