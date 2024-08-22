from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import json
import matplotlib.pyplot as plt
import io
import base64
import requests
from datetime import datetime
from models import Transaction, load_transactions, save_transactions, get_exchange_rate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class TransactionForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    type = SelectField('Type', choices=[('income', 'Income'), ('expense', 'Expense')], validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    amount = DecimalField('Amount', places=2, validators=[DataRequired(), NumberRange(min=0)])
    currency = SelectField('Currency', choices=[('PLN', 'PLN'), ('USD', 'USD'), ('EUR', 'EUR')], validators=[DataRequired()])
    submit = SubmitField('Submit')

def convert_to_pln(amount, currency):
    rate = get_exchange_rate(currency)
    return amount * rate if rate else amount

@app.route('/')
def index():
    transactions = load_transactions()
    balance = sum(
        convert_to_pln(t.amount, t.currency) if t.type == 'income' else -convert_to_pln(t.amount, t.currency)
        for t in transactions
    )
    return render_template('view_budget.html', transactions=transactions, balance=balance)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        transaction = Transaction(
            date=form.date.data,
            type=form.type.data,
            description=form.description.data,
            amount=form.amount.data,
            currency=form.currency.data
        )
        transactions = load_transactions()
        transactions.append(transaction)
        save_transactions(transactions)
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_transaction.html', form=form)

@app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    transactions = load_transactions()
    transaction = transactions[transaction_id]
    form = TransactionForm(obj=transaction)
    if form.validate_on_submit():
        transaction.date = form.date.data
        transaction.type = form.type.data
        transaction.description = form.description.data
        transaction.amount = form.amount.data
        transaction.currency = form.currency.data
        save_transactions(transactions)
        flash('Transaction updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_transaction.html', form=form)

@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    transactions = load_transactions()
    transactions.pop(transaction_id)
    save_transactions(transactions)
    flash('Transaction deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/chart')
def chart():
    transactions = load_transactions()
    income = [convert_to_pln(t.amount, t.currency) for t in transactions if t.type == 'income']
    expenses = [convert_to_pln(t.amount, t.currency) for t in transactions if t.type == 'expense']
    
    fig, ax = plt.subplots()
    ax.plot(range(len(income)), income, label='Income', color='green')
    ax.plot(range(len(expenses)), expenses, label='Expense', color='red')
    ax.set_xlabel('Transaction Index')
    ax.set_ylabel('Amount (PLN)')
    ax.set_title('Income and Expenses')
    ax.legend()

    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    return render_template('chart.html', img_data=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
