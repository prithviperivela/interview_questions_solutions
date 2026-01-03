import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive")
            return
    except ValueError:
        print("Invalid amount")
        return

    category = input("Enter category: ").strip()
    note = input("Enter note: ").strip()

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "note": note
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded")
        return

    print("\nDate       Amount   Category   Note")
    print("--------------------------------------")

    for exp in expenses:
        print(f"{exp['date']}  {exp['amount']:7.2f}  {exp['category']:8}  {exp['note']}")


def view_total_spending(expenses):
    total = 0
    for exp in expenses:
        total += exp["amount"]

    print(f"\nTotal Spending: {total:.2f}")


def view_spending_by_category(expenses):
    category_totals = {}

    for exp in expenses:
        category = exp["category"]
        amount = exp["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\nSpending by Category:")
    for category in category_totals:
        print(f"{category}: {category_totals[category]:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. View Spending by Category")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total_spending(expenses)
        elif choice == "4":
            view_spending_by_category(expenses)
        elif choice == "5":
            print("Exiting program")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
