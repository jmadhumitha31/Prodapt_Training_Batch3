import csv
from expense import Expense
from exceptions import InvalidAmountError


class ExpenseManager(Expense):

    def __init__(self):
        self.filename = "expenses.csv"
        self.create_file()

    # Create CSV file if it doesn't exist
    def create_file(self):
        try:
            with open(self.filename, "r"):
                pass
        except FileNotFoundError:
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["expense_id", "date", "category", "description", "amount"]
                )

    # Add Expense
    def add_expense(self):
        try:
            expense_id = int(input("Enter Expense ID: "))
            date = input("Enter Date (DD-MM-YYYY): ")
            category = input("Enter Category: ")
            description = input("Enter Description: ")
            amount = float(input("Enter Amount: "))

            expense = Expense(
                expense_id,
                date,
                category,
                description,
                amount
            )

            with open(self.filename, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(expense.to_list())

            print("Expense Added Successfully.")

        except InvalidAmountError as e:
            print(e)

        except ValueError:
            print("Invalid Input.")

    # View Expenses
    def view_expense(self):
       try:
           with open(self.filename, "r", newline="") as file:
            reader = csv.reader(file)

            rows = list(reader)

            if len(rows) <= 1:
                print("No Expense Records Found.")
                return

            print("\n------------------------------")
            print("Expense Records")
            print("------------------------------")

            for row in rows:
                print(row)

       except FileNotFoundError:
           print("File Not Found.")

    # Search by Category
    def search_category(self):
        category = input("Enter Category: ")

        found = False

        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                if row["category"].lower() == category.lower():
                    print(row)
                    found = True

        if not found:
            print("No Record Found.")

    # Update Expense
    def update_expense(self):
        expense_id = input("Enter Expense ID: ")

        rows = []
        found = False

        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:

                if row["expense_id"] == expense_id:

                    row["description"] = input("New Description: ")
                    row["amount"] = input("New Amount: ")

                    found = True

                rows.append(row)

        if found:

            with open(self.filename, "w", newline="") as file:

                fieldnames = [
                    "expense_id",
                    "date",
                    "category",
                    "description",
                    "amount"
                ]

                writer = csv.DictWriter(file, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(rows)

            print("Expense Updated Successfully.")

        else:
            print("Expense ID Not Found.")

    # Delete Expense
    def delete_expense(self):
        expense_id = input("Enter Expense ID: ")

        rows = []
        found = False

        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:

                if row["expense_id"] != expense_id:
                    rows.append(row)
                else:
                    found = True

        with open(self.filename, "w", newline="") as file:

            fieldnames = [
                "expense_id",
                "date",
                "category",
                "description",
                "amount"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(rows)

        if found:
            print("Expense Deleted Successfully.")
        else:
            print("Expense ID Not Found.")

    # Monthly Summary
    def monthly_summary(self):
        month = input("Enter Month (MM): ")

        total = {}

        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:

                if row["date"][3:5] == month:

                    category = row["category"]
                    amount = float(row["amount"])

                    if category in total:
                        total[category] += amount
                    else:
                        total[category] = amount

        print("\nMonthly Summary\n")

        for category, amount in total.items():
            print(category, ":", amount)