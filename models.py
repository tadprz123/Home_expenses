import json
from decimal import Decimal

class Expenses:
    def __init__(self):
        try:
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []

    def all(self):
        return self.expenses

    def get(self, id):
        return self.expenses[id]

    def create(self, data):
        data.pop('csrf_token')
        data['amount'] = float(data['amount'])  # Konwersja Decimal na float
        self.expenses.append(data)
        self.save_all()

    def save_all(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f)

    def update(self, id, data):
        data.pop('csrf_token')
        data['amount'] = float(data['amount'])  # Konwersja Decimal na float
        self.expenses[id] = data
        self.save_all()

expenses = Expenses()