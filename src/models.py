import csv
from datetime import datetime
from collections import defaultdict
import os

class Expense:
    def __init__(self, category, amount, date=None):
        self.category = category
        self.amount = float(amount)
        self.date = date if date else datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')}, {self.category}, ${self.amount:.2f}"

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount):
        expense = Expense(category, amount)
        self.expenses.append(expense)
        print(f"Added: {expense}")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            deleted_expense = self.expenses.pop(index)
            print(f"Deleted: {deleted_expense}")
        else:
            print("Invalid index.")

    def show_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, expense in enumerate(self.expenses):
            print(f"{i}: {expense}")

    def generate_report(self, time_period):
        report = defaultdict(float)
        for expense in self.expenses:
            if time_period == 'daily':
                period = expense.date.date()
            elif time_period == 'weekly':
                period = expense.date.strftime('%Y-%W')
            elif time_period == 'yearly':
                period = expense.date.year
            else:
                print("Invalid time period.")
                return
            report[period] += expense.amount
        
        for period, total in report.items():
            print(f"{period}: ${total:.2f}")

    def save_to_csv(self, filename='data/expenses.csv'):
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount'])
            for expense in self.expenses:
                writer.writerow([expense.date.strftime('%Y-%m-%d'), expense.category, expense.amount])
        print(f"Saved expenses to {filename}.")

    def load_from_csv(self, filename='data/expenses.csv'):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    date, category, amount = row
                    self.expenses.append(Expense(category, amount, datetime.strptime(date, '%Y-%m-%d')))
            print(f"Loaded expenses from {filename}.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
