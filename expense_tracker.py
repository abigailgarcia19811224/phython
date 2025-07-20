import csv
from datetime import datetime
from typing import List, Dict

Transaction = Dict[str, str]


def add_transaction(transactions: List[Transaction]) -> None:
    date = input("Date (YYYY-MM-DD) [today]: ") or datetime.today().strftime('%Y-%m-%d')
    category = input("Category: ")
    description = input("Description: ")
    amount = input("Amount: ")
    transactions.append({
        'date': date,
        'category': category,
        'description': description,
        'amount': amount
    })
    print("Transaction added.\n")


def view_transactions(transactions: List[Transaction]) -> None:
    if not transactions:
        print("No transactions recorded.\n")
        return
    print("Transactions:")
    for t in transactions:
        print(f"{t['date']} | {t['category']} | {t['description']} | {t['amount']}")
    print()


def export_to_csv(transactions: List[Transaction]) -> None:
    if not transactions:
        print("No transactions to export.\n")
        return
    filename = input("Enter filename to export to [expenses.csv]: ") or "expenses.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['date', 'category', 'description', 'amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    print(f"Transactions exported to {filename}.\n")


def main() -> None:
    transactions: List[Transaction] = []
    menu = (
        "1. Add transaction\n"
        "2. View transactions\n"
        "3. Export to CSV\n"
        "4. Quit"
    )
    while True:
        print(menu)
        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            export_to_csv(transactions)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
