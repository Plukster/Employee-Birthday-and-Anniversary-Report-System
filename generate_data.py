import csv
from datetime import datetime, timedelta
import random

def generate_sample_data():
    # Sample employee data
    employees = [
        {"name": "John Smith", "hire_date": "2020-03-15", "department": "HR", "birthday": "1985-04-10"},
        {"name": "Jane Doe", "hire_date": "2019-07-22", "department": "Finance", "birthday": "1990-04-25"},
        {"name": "Bob Johnson", "hire_date": "2021-01-10", "department": "Engineering", "birthday": "1988-04-05"},
        {"name": "Alice Brown", "hire_date": "2018-11-30", "department": "Finance", "birthday": "1992-04-18"},
        {"name": "Charlie Wilson", "hire_date": "2022-02-14", "department": "Marketing", "birthday": "1995-04-30"},
        {"name": "Diana Lee", "hire_date": "2020-06-08", "department": "R&D", "birthday": "1987-04-12"},
        {"name": "Eve Davis", "hire_date": "2019-09-20", "department": "Operations", "birthday": "1993-04-22"},
        {"name": "Frank Miller", "hire_date": "2021-05-17", "department": "Engineering", "birthday": "1986-04-08"},
        {"name": "Grace Wilson", "hire_date": "2020-08-13", "department": "Finance", "birthday": "1991-04-15"},
        {"name": "Henry Taylor", "hire_date": "2019-12-05", "department": "HR", "birthday": "1989-04-28"},
        {"name": "Ivy Chen", "hire_date": "2022-03-11", "department": "Marketing", "birthday": "1994-04-17"},
        {"name": "Jack Anderson", "hire_date": "2018-04-19", "department": "R&D", "birthday": "1990-04-20"},
        {"name": "Kate Thomas", "hire_date": "2021-07-25", "department": "Operations", "birthday": "1988-04-03"},
        {"name": "Liam Jackson", "hire_date": "2020-01-30", "department": "Engineering", "birthday": "1992-04-11"},
        {"name": "Mia White", "hire_date": "2019-05-14", "department": "Finance", "birthday": "1987-04-29"},
        {"name": "Noah Harris", "hire_date": "2022-09-07", "department": "HR", "birthday": "1993-04-06"},
        {"name": "Olivia Martin", "hire_date": "2021-11-22", "department": "Marketing", "birthday": "1989-04-14"},
        {"name": "Paul Thompson", "hire_date": "2018-10-31", "department": "R&D", "birthday": "1995-04-21"},
        {"name": "Quinn Garcia", "hire_date": "2020-02-16", "department": "Operations", "birthday": "1991-04-09"},
        {"name": "Ryan Rodriguez", "hire_date": "2019-08-12", "department": "Engineering", "birthday": "1986-04-23"},
    ]
    
    # Write to CSV file
    with open('database.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'hire_date', 'department', 'birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for employee in employees:
            writer.writerow(employee)

if __name__ == "__main__":
    generate_sample_data()
    print("Sample data generated in database.csv")