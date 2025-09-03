import csv
import sys
from datetime import datetime

def get_month_number(month_name):
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    return months.get(month_name.lower(), 0)

def read_employees(filename):
    employees = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)
    return employees

def get_birthdays_and_anniversaries(employees, month):
    birthdays = []
    anniversaries = []
    
    target_month = get_month_number(month)
    
    for employee in employees:
        # Parse birthday
        birthday_str = employee['birthday']
        try:
            birthday = datetime.strptime(birthday_str, '%Y-%m-%d')
        except ValueError:
            continue
            
        # Parse hire date
        hire_date_str = employee['hire_date']
        try:
            hire_date = datetime.strptime(hire_date_str, '%Y-%m-%d')
        except ValueError:
            continue
        
        # Check if birthday is in the target month
        if birthday.month == target_month:
            birthdays.append({
                'name': employee['name'],
                'department': employee['department']
            })
        
        # Check if anniversary is in the target month
        # For anniversary, we compare the month and day (ignoring year)
        if hire_date.month == target_month:
            anniversaries.append({
                'name': employee['name'],
                'department': employee['department']
            })
    
    return birthdays, anniversaries

def group_by_department(employees_list):
    department_dict = {}
    for employee in employees_list:
        dept = employee['department']
        if dept not in department_dict:
            department_dict[dept] = []
        department_dict[dept].append(employee['name'])
    return department_dict

def print_report(employees, month):
    birthdays, anniversaries = get_birthdays_and_anniversaries(employees, month)
    
    print(f"Report for {month.capitalize()} generated")
    print("--- Birthdays ---")
    
    if birthdays:
        birthday_by_dept = group_by_department(birthdays)
        total_birthday = len(birthdays)
        print(f"Total: {total_birthday}")
        print("By department:")
        for dept in sorted(birthday_by_dept.keys()):
            names = ", ".join(birthday_by_dept[dept])
            print(f"- {dept}: {len(birthday_by_dept[dept])}")
            print(f"  Employees: {names}")
    else:
        print("Total: 0")
        print("By department:")
    
    print("--- Anniversaries ---")
    
    if anniversaries:
        anniversary_by_dept = group_by_department(anniversaries)
        total_anniversary = len(anniversaries)
        print(f"Total: {total_anniversary}")
        print("By department:")
        for dept in sorted(anniversary_by_dept.keys()):
            names = ", ".join(anniversary_by_dept[dept])
            print(f"- {dept}: {len(anniversary_by_dept[dept])}")
            print(f"  Employees: {names}")
    else:
        print("Total: 0")
        print("By department:")

def main():
    if len(sys.argv) != 3:
        print("Usage: python report.py <database_file> <month>")
        sys.exit(1)
    
    database_file = sys.argv[1]
    month = sys.argv[2]
    
    employees = read_employees(database_file)
    print_report(employees, month)

if __name__ == "__main__":
    main()