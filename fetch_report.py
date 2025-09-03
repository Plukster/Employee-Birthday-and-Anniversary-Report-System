import sys
import requests
from datetime import datetime

def fetch_report(month, department):
    try:
        # Make request to the API
        url = f"http://localhost:5000/birthdays?month={month}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Error: Failed to fetch data (HTTP {response.status_code})")
            return
        
        data = response.json()
        
        
        try:
            import csv
            birthdays = []
            
            with open('database.csv', 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                
                for row in reader:
                    
                    if row.get('department') == department:
                       
                        if 'birthday' in row and row['birthday']:
                            try:
                                # Parse birthday (assuming format is YYYY-MM-DD)
                                birth_date = datetime.strptime(row['birthday'], '%Y-%m-%d')
                                if birth_date.month == get_month_number(month):
                                    birthdays.append({
                                        'name': row.get('name', 'Unknown'),
                                        'date': birth_date.strftime('%b %d')
                                    })
                            except (ValueError, IndexError):
                                continue
            
            # Sort by date
            birthdays.sort(key=lambda x: datetime.strptime(x['date'], '%b %d'))
            
            print(f"Report for {department} department for {month.capitalize()} fetched.")
            print(f"Total: {len(birthdays)}")
            print("Employees:")
            for emp in birthdays:
                print(f"- {emp['date']}, {emp['name']}")
                
        except FileNotFoundError:
            print("Error: Database file not found")
            return
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure it's running on port 5000.")
    except Exception as e:
        print(f"Error: {e}")

def get_month_number(month_name):
    months = {
        'january': 1, 'february': 2, 'march': 3, 'april': 4,
        'may': 5, 'june': 6, 'july': 7, 'august': 8,
        'september': 9, 'october': 10, 'november': 11, 'december': 12
    }
    return months.get(month_name.lower(), 0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fetch_report.py <month> <department>")
        sys.exit(1)
    
    month = sys.argv[1]
    department = sys.argv[2]
    
    fetch_report(month, department)