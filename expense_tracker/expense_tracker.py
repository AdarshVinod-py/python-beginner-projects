import sqlite3
from typing import Optional , Any
from expense import Expense

class ExpenseTracker:
    def __init__(self, connection : sqlite3.Connection, cursor : sqlite3.Cursor) -> None:
        self.connection = connection
        self.cursor = cursor

    def add_expense(self, expense : Expense) -> int | None:
        self.cursor.execute("""
        INSERT INTO expenses (amount, category_id, date, description) VALUES (?, ?, ?, ?)""",(expense.amount, expense.category_id, expense.date, expense.description))
        self.connection.commit()
        last_id = self.cursor.lastrowid
        return last_id

    def view_expenses(self, category_id : Optional[int] = None, start_date : Optional[str] = None, end_date : Optional[str] = None ) -> list:
        query = "SELECT * FROM expenses WHERE 1 = 1"
        parameter = []
        if category_id is not None:
            query += " AND category_id = ?"
            parameter.append(category_id)
        if start_date is not None and end_date is not None:
            query += " AND date BETWEEN ? AND ?"
            parameter.append(start_date)
            parameter.append(end_date)
        elif start_date is not None:
            query += " AND date >= ?"
            parameter.append(start_date)
        elif end_date is not None:
            query += " AND date <= ?"
            parameter.append(end_date)

        self.cursor.execute(query,parameter)
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            single_expense = Expense(id=row[0], amount= row[1], category_id= row[2], date= row[3], description= row[4])
            result.append(single_expense)
            
        return result

    def update_expense(self,expense_id : int, **kwargs : Any) -> int:
        column_names = []
        values_to_update = []
        if not kwargs:
            return 0
        for key,value in kwargs.items():
            column_names.append(f"{key} = ?")
            values_to_update.append(value)
        set_clause = ", ".join(column_names)
        values_to_update.append(expense_id)
        query = f"UPDATE expenses SET {set_clause} WHERE id = ?"
        self.cursor.execute(query,values_to_update)
        self.connection.commit()
        row_count = self.cursor.rowcount
        return row_count

    def delete_expense(self,expense_id : int) -> int:
        query = "DELETE FROM expenses WHERE id = ?"
        value = [expense_id]
        self.cursor.execute(query,value)
        self.connection.commit()
        row_count = self.cursor.rowcount
        return row_count

    def view_total(self, category_id : Optional[int] = None, start_date : Optional[str] = None, end_date : Optional[str] = None ) -> float:
        query = "SELECT SUM(amount) FROM expenses WHERE 1 = 1"
        parameter = []
        if category_id is not None:
            query += " AND category_id = ?"
            parameter.append(category_id)
        if start_date is not None and end_date is not None:
            query += " AND date BETWEEN ? AND ?"
            parameter.append(start_date)
            parameter.append(end_date)
        elif start_date is not None:
            query += " AND date >= ?"
            parameter.append(start_date)
        elif end_date is not None:
            query += " AND date <= ?"
            parameter.append(end_date)

        self.cursor.execute(query,parameter)
        result = self.cursor.fetchone()

        if result[0] is None:
            return 0
        return result[0]