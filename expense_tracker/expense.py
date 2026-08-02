from datetime import datetime
from typing import Optional


class Expense:
    def __init__(self,  amount : float, category_id : int,  description : str, id : Optional[int] = None , date : Optional[str] = None,) -> None:
        self.amount = amount
        self.category_id = category_id
        self.description = description
        self.id = id
        if date is None:
            self.date = datetime.today().strftime("%Y-%m-%d")
        else:
            self.date = date
