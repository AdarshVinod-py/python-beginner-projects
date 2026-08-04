import sqlite3
from typing import Optional

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

    def view_expenses(self, category_id : Optional[int] = None, start_date : Optional[str] = None, end_date : Optional[str] = None ):
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
