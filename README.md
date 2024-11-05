# Expense Tracker Application

## Overview
The Expense Tracker Application is a CLI-based tool developed as part of the midcourse project for Fynd Academy. This application enables users to manage and categorize their daily expenses efficiently. It incorporates Python fundamentals, object-oriented programming, file handling with CSV, and data persistence. The main objective is to provide an easy-to-use tool for tracking, analyzing, and reporting expenses.

## Objectives
- Allow users to add, categorize, view, update, and delete expenses.
- Enable filtering of expenses by categories.
- Generate reports for specific time periods (daily, weekly, monthly).
- Provide data persistence using CSV files.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/expense-tracker.git
   cd expense-tracker
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
python src/tracker.py
> Enter amount: 50.00
> Enter date (YYYY-MM-DD): 2024-11-01
> Enter category: Groceries
> Enter description: Bought fruits and vegetables
