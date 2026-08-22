from database import create_connection
from expense_tracker import ExpenseTracker
from expense import Expense

connection, cursor = create_connection()
tracker = ExpenseTracker(connection,cursor)

def add_expense_ui(tracker : ExpenseTracker)-> None:
    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Please Enter amount in digits")
    tracker.cursor.execute("SELECT * FROM categories")
    categories = tracker.cursor.fetchall()
    print(f"\n{"ID" :>5} - Category")
    print("-"*20)
    for id, name in categories:
        print(f"{id :>5} - {name}")
    valid_ids = [id for id, name in categories]
    while True:
        try:
            category = int(input("\nEnter Category ID: "))
            if category not in valid_ids:
                print("Invalid ID")
            else:
                break
        except ValueError:
            print("Invalid Category ID")
            
    description = input("Enter Description: ")
    if description == "":
        description = None
    expense = Expense(amount=amount, category_id=category, description=description)
    expense_id = tracker.add_expense(expense=expense)
    if expense_id is None:
        print("Failed to add Expense")
    else:
        print(f"Expense added sucessfully. ID ={expense_id}")


