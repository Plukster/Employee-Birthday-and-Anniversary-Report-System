from flask import Flask, request, jsonify
import csv
from datetime import datetime

app = Flask(__name__)

def get_month_number(month_name):
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    return months.get(month_name.lower(), 0)

@app.route('/birthdays')
def get_birthdays_report():
    month = request.args.get('month', '').lower()
    
    if not month:
        return jsonify({"error": "Month parameter is required"}), 400
    
    month_num = get_month_number(month)
    if month_num == 0:
        return jsonify({"error": f"Invalid month: {month}"}), 400
    
    birthdays = []
    anniversaries = []
    
    try:
        with open('database.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            for row in reader:
                # Process birthday
                try:
                    if 'birthday' in row and row['birthday']:
                        birthday_str = f"2023-{row['birthday'][-5:]}"  # Extract MM-DD
                        birth_date = datetime.strptime(birthday_str, '%Y-%m-%d')
                        if birth_date.month == month_num:
                            birthdays.append(row)
                except (ValueError, IndexError):
                    continue
                
                # Process anniversary
                try:
                    if 'hire_date' in row and row['hire_date']:
                        hire_date = datetime.strptime(row['hire_date'], '%Y-%m-%d')
                        if hire_date.month == month_num:
                            anniversaries.append(row)
                except (ValueError, IndexError):
                    continue
    
    except FileNotFoundError:
        return jsonify({"error": "Database file not found"}), 500
    except Exception as e:
        return jsonify({"error": f"Error reading file: {str(e)}"}), 500
    
    # Group by department
    birthday_by_dept = {}
    for emp in birthdays:
        dept = emp.get('department', 'Unknown')
        birthday_by_dept[dept] = birthday_by_dept.get(dept, 0) + 1
    
    anniversary_by_dept = {}
    for emp in anniversaries:
        dept = emp.get('department', 'Unknown')
        anniversary_by_dept[dept] = anniversary_by_dept.get(dept, 0) + 1
    
    # Return JSON response
    result = {
        "month": month.capitalize(),
        "birthdays": {
            "total": len(birthdays),
            "by_department": birthday_by_dept
        },
        "anniversaries": {
            "total": len(anniversaries),
            "by_department": anniversary_by_dept
        }
    }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)