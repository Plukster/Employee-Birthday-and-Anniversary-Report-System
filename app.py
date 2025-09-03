from flask import Flask, request, jsonify
import csv
import sys
from datetime import datetime

app = Flask(__name__)

def read_employee_data(filename='database.csv'):
    employees = []
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Clean up the row data to handle any inconsistencies
                cleaned_row = {}
                for key, value in row.items():
                    if key.strip():  # Only include non-empty keys
                        cleaned_row[key.strip()] = value.strip()
                employees.append(cleaned_row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    return employees

def get_month_number(month_name):
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    return months.get(month_name.lower(), 0)

def get_birthdays(month, department=None):
    employees = read_employee_data()
    month_num = get_month_number(month)
    
    if month_num == 0:
        return []
    
    result = []
    for i, employee in enumerate(employees):
        # Check if employee has required fields
        if 'birthday' not in employee or 'name' not in employee:
            continue
            
        try:
            # Check if birthday is in the specified month
            birthday_parts = employee['birthday'].split('-')
            if len(birthday_parts) >= 2:
                birthday_month = int(birthday_parts[0])
                if birthday_month == month_num:
                    # Filter by department if specified
                    if department is None or employee.get('department') == department:
                        # Format date for display
                        try:
                            date_obj = datetime.strptime(employee['birthday'], '%m-%d')
                            formatted_date = date_obj.strftime('%b %d')
                        except ValueError:
                            formatted_date = employee['birthday']
                        
                        result.append({
                            "id": i + 1,
                            "name": employee['name'],
                            "birthday": formatted_date
                        })
        except (ValueError, IndexError):
            continue
    
    return result

def get_anniversaries(month, department=None):
    employees = read_employee_data()
    month_num = get_month_number(month)
    
    if month_num == 0:
        return []
    
    result = []
    for i, employee in enumerate(employees):
        # Check if employee has required fields
        if 'hiring_date' not in employee and 'hire_date' not in employee:
            continue
            
        try:
            # Check if hire date is in the specified month
            hire_date_field = 'hiring_date' if 'hiring_date' in employee else 'hire_date'
            
            # Handle different date formats
            hire_date_str = employee[hire_date_field]
            if '-' in hire_date_str:
                hire_date = datetime.strptime(hire_date_str, '%Y-%m-%d')
            elif '/' in hire_date_str:
                hire_date = datetime.strptime(hire_date_str, '%m/%d/%Y')
            else:
                continue
                
            if hire_date.month == month_num:
                # Filter by department if specified
                if department is None or employee.get('department') == department:
                    # Format date for display
                    formatted_date = hire_date.strftime('%b %d')
                    
                    result.append({
                        "id": i + 1,
                        "name": employee['name'],
                        "hire_date": formatted_date
                    })
        except (ValueError, KeyError):
            continue
    
    return result

@app.route('/birthdays', methods=['GET'])
def get_birthdays_endpoint():
    month = request.args.get('month')
    department = request.args.get('department')
    
    if not month:
        return jsonify({"error": "Month parameter is required"}), 400
    
    birthdays = get_birthdays(month, department)
    
    response = {
        "total": len(birthdays),
        "employees": birthdays
    }
    
    return jsonify(response)

@app.route('/anniversaries', methods=['GET'])
def get_anniversaries_endpoint():
    month = request.args.get('month')
    department = request.args.get('department')
    
    if not month:
        return jsonify({"error": "Month parameter is required"}), 400
    
    anniversaries = get_anniversaries(month, department)
    
    response = {
        "total": len(anniversaries),
        "employees": anniversaries
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)