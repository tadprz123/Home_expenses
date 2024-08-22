import json
import requests
from datetime import datetime

class Transaction:
    def __init__(self, date, type, description, amount, currency):
        self.date = date
        self.type = type
        self.description = description
        self.amount = amount
        self.currency = currency

    def to_dict(self):
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'type': self.type,
            'description': self.description,
            'amount': float(self.amount),
            'currency': self.currency
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            date=datetime.strptime(data['date'], '%Y-%m-%d'),
            type=data['type'],
            description=data['description'],
            amount=data['amount'],
            currency=data['currency']
        )

def load_transactions():
    try:
        with open('transactions.json', 'r') as f:
            data = json.load(f)
            return [Transaction.from_dict(d) for d in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: JSON file is not readable or contains invalid JSON.")
        return []

def save_transactions(transactions):
    with open('transactions.json', 'w') as f:
        json.dump([t.to_dict() for t in transactions], f, indent=4)

def get_exchange_rate(currency_code):
    if currency_code == 'PLN':
        return 1.0
    url = f'http://api.nbp.pl/api/exchangerates/rates/A/{currency_code}/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['rates'][0]['mid']
    except (requests.RequestException, KeyError):
        print(f"Error fetching exchange rate for {currency_code}.")
        return None
