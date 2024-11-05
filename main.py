from models import ExpenseTracker

def main():
    tracker = ExpenseTracker()
    
    # Load existing expenses
    tracker.load_from_csv()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Delete Expense")
        print("3. Show Expenses")
        print("4. Generate Report")
        print("5. Save and Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            category = input("Enter category (e.g., Groceries, Utilities, Entertainment, Others): ")
            amount = float(input("Enter amount: "))
            tracker.add_expense(category, amount)
        
        elif choice == '2':
            tracker.show_expenses()
            index = int(input("Enter the index of the expense to delete: "))
            tracker.delete_expense(index)

        elif choice == '3':
            tracker.show_expenses()

        elif choice == '4':
            time_period = input("Enter time period (daily, weekly, yearly): ")
            tracker.generate_report(time_period)

        elif choice == '5':
            tracker.save_to_csv()
            print("Expenses saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()