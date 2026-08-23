from database import create_connection
from expense_tracker import ExpenseTracker
from expense import Expense

connection, cursor = create_connection()
tracker = ExpenseTracker(connection,cursor)
tracker.cursor.execute("SELECT * FROM categories")
categories = tracker.cursor.fetchall()
valid_ids = [id for id, name in categories]

def view_categories()-> None:
    print(f"\n{'ID' :>5} - Category")
    print("-"*20)
    for id, name in categories:
        print(f"{id :>5} - {name}")

def select_category()-> int:  
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
    view_categories()
    category = select_category()

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
                    view_categories()
                    category = select_category()
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

def update_expenses_ui() -> None:
    while True:
        try:
            expense_id = int(input("Enter Expense ID to update expense: "))
            break
        except ValueError:
            print("Invalid Input")
    expenses = tracker.view_expenses()
    valid_id = [expense.id for expense in expenses]
    if expense_id not in valid_id:
        print("Expense not found")
    else:
        print("Enter Values to update(Press 'Enter' to skip a section\n)")
        while True:
            amount = input("Enter Amount: ")
            if amount != "":
                try:
                    amount = float(amount)
                    break
                except ValueError:
                    print("Enter a valid Amount in digits: ")
            elif amount == "":
                break
        view_categories()        
        while True:
            category = input("Enter Category ID: ")
            if category != "":
                try:
                    category = int(category)
                    if category in valid_ids:
                      break
                    else: 
                        print("Enter a valid ID: ")
                except ValueError:
                    print("Invalid Category ID")
            elif category == "":
                break
        description = input("Enter Description: ")
        date = input("Enter Date (YYYY-MM-DD): ")
        row_count = tracker.update_expense(expense_id=expense_id, amount=amount, category_id=category, date= date,description=description)
        if row_count == 1:
            print("Expense updated sucessfully")
        elif row_count == 0:
            print("Expense was not updated")

def delete_expense_ui()-> None:
    while True:
        try:
            expense_id = int(input("Enter Expense ID to delete expense: "))
            break
        except ValueError:
            print("Invalid Input")
    expenses = tracker.view_expenses()
    valid_id = [expense.id for expense in expenses]
    if expense_id not in valid_id:
        print("Expense not found")
    else:
        validation = input("Are you sure you want to delete this expense? (y/n): ")
        if validation == 'y':
            row_count = tracker.delete_expense(expense_id=expense_id)
            if row_count == 1:
                print("Expense deleted sucessfully")
            elif row_count == 0:
                print("Failed to delete expense")  
        else:
            print("Delete was cancelled")          

def view_total_ui()->None :
    while True:
        filters = input("Do you want to add Filters?(y/n): ")

        if filters == 'n':
            total = tracker.view_total()
            print(f"Total : {total :.2f} Rs")
            break

        elif filters == 'y':
            while True:
                which_filter = input("Enter 'c' to filter by categories,\nEnter 'd' to filter with dates: ")
                if which_filter == 'c':
                    view_categories()
                    category = select_category()
                    total = tracker.view_total(category_id=category)
                    print(f"Total : {total :.2f} Rs")
                    break  
                    
                elif which_filter == 'd':
                    start_date = input("Enter start date (YYYY-MM-DD): ")
                    end_date = input("Enter end date (YYYY-MM-DD): ")
                    if start_date == "":
                        start_date = None
                    if end_date == "":
                        end_date = None

                    total = tracker.view_total(start_date=start_date,end_date=end_date)
                    print(f"Total : {total :.2f} Rs")
                    break

                else:
                    print("Invalid choice")
            break
        else:
            print("Invalid Choice")      

