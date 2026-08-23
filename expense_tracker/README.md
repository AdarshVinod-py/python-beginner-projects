# Expense Tracker
It's a CLI tool which can be used to record your expenses and classify them into different categories.

## Features:
 - Add, view, update and delete expense records
 - Filter expenses by categories and dates
 - Calculate total expenses in each category/dates
 
## Tech stack:
 - Python
 - SQLite

## How to run:
```bash
git clone https://github.com/adarshvinod-devs/learning_python.git
cd learning_python/expense_tracker
python main.py
```
## Project structure:
 - main.py contains the menu loop
 - ui.py contains functions for user interactions
 - expense_tracker.py is the data layer
 - expense.py contains data model
 - database.py contains database connection/setup

## What I learned:
This was the 1st project in which I used multiple modules, Classes and SQL properly. Learned to build Dynamic SQL queries, learned to use objects, learned to separate functions and user inputs/outputs. Tried to reduced redundancy.