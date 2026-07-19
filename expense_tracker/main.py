from expense_manager import ExpenseManager

manager = ExpenseManager()

while True:

    print("\n========== PERSONAL EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search by Category")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Monthly Summary")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            manager.add_expense()

        elif choice == 2:
            manager.view_expense()

        elif choice == 3:
            manager.search_category()

        elif choice == 4:
            manager.update_expense()

        elif choice == 5:
            manager.delete_expense()

        elif choice == 6:
            manager.monthly_summary()

        elif choice == 7:
            print("Thank you for using Personal Expense Tracker.")
            break

        else:
            print("Please Enter a Valid Choice.")

    except ValueError:
        print("Please Enter Numbers Only.")