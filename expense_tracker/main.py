from database import create_connection
from expense_tracker import ExpenseTracker
from expense import Expense

connection, cursor = create_connection()
tracker = ExpenseTracker(connection,cursor)

def select_categories()-> int:
    tracker.cursor.execute("SELECT * FROM categories")
    categories = tracker.cursor.fetchall()
    print(f"\n{'ID' :>5} - Category")
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
                return category
        except ValueError:
            print("Invalid Category ID")

def display_expenses(expenses : list)->None:
        if not expenses:
            print("No Expenses Found\n")
        else:
            tracker.cursor.execute("SELECT * FROM categories")
            categories_dict = {id : name for id,name in tracker.cursor.fetchall()}
            print(f"{'ID':<5}{'Amount':<8}{'Category':<12}{'Date':<15}{'Description':<15}")
            print("-"*55)
            for row in expenses:
                print(f"{row.id:<5}{row.amount:<8}{categories_dict[row.category_id]:<12}{row.date:<15}{"" if row.description is None else row.description}")


def add_expense_ui()-> None:
    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Please Enter amount in digits")

    category = select_categories()

    description = input("Enter Description: ")
    if description == "":
        description = None

    expense = Expense(amount=amount, category_id=category, description=description)
    expense_id = tracker.add_expense(expense=expense)
    if expense_id is None:
        print("Failed to add Expense")
    else:
        print(f"Expense added sucessfully. ID ={expense_id}\n")

def view_expense_ui()-> None:
    while True:
        filters = input("Do you want to add Filters?(y/n): ")

        if filters == 'n':
            expenses = tracker.view_expenses()
            display_expenses(expenses)
            break

        elif filters == 'y':
            while True:
                which_filter = input("Enter 'c' to filter by categories,\nEnter 'd' to filter with dates: ")
                if which_filter == 'c':
                    category = select_categories()
                    expenses = tracker.view_expenses(category_id=category)
                    display_expenses(expenses)
                    break  
                    
                elif which_filter == 'd':
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    if start_date == "":
                        start_date = None
                    if end_date == "":
                        end_date = None

                    expenses = tracker.view_expenses(start_date=start_date,end_date=end_date)
                    display_expenses(expenses)
                    break

                else:
                    print("Invalid choice")
            break
        else:
            print("Invalid Choice")            

            

#add_expense_ui()
view_expense_ui()