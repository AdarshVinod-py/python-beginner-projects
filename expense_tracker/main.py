import ui

menu = "\n1 -> Add Expense\n2 -> View Expense\n3 -> View Total\n4 -> Update Expense\n5 -> Delete Expense\n0 -> Exit"
while True:
    try:
        print(menu)
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                ui.add_expense_ui()
            case 2:
                ui.view_expense_ui()
            case 3:
                ui.view_total_ui()
            case 4:
                ui.update_expenses_ui()
            case 5:
                ui.delete_expense_ui()
            case 0:
                break
            case _:
                print("Invalid Choice")
    except ValueError:
        print("Invalid Choice")