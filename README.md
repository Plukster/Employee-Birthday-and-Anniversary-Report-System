# Employee Birthday and Anniversary Report System

This project automates the process of generating reports for employee birthdays and hiring anniversaries, replacing the manual paper-based system with a digital solution.

## Features

- **Data Generation**: Creates synthetic employee data including names, departments, hire dates, and birthdays
- **Report Generation**: Automatically generates monthly reports showing birthdays and anniversaries by department
- **Digital Automation**: Eliminates the need to manually search through paper archives

## Files

### `generate_data.py`
Generates synthetic employee data and writes it to `database.csv`

**Features:**
- Creates 100 employee records with realistic data
- Includes name, department, hire date, and birthday
- Randomizes departments (HR, Finance, Engineering, R&D)
- Generates realistic dates for hiring and birthdays

### `report.py`
Generates monthly reports for birthdays and anniversaries

**Usage:**
```bash
python report.py database.csv april
```
**Output Format:**
```
Report for April generated
--- Birthdays ---
Total: 45
By department:
- HR: 10
- Finance: 15
- Engineering: 20
--- Anniversaries ---
Total: 31
By department:
- Finance: 5
- R&D: 10
- Engineering: 16
```
## Run web server for API access:
```
python web_app.py

Then visit http://localhost:5000/birthdays?month=april to get JSON response.
```
**Output Format:**
```
{
  "anniversaries": {
    "by_department": {
      "R&D": 1
    },
    "total": 1
  },
  "birthdays": {
    "by_department": {
      "Engineering": 4,
      "Finance": 4,
      "HR": 3,
      "Marketing": 3,
      "Operations": 3,
      "R&D": 3
    },
    "total": 20
  },
  "month": "April"
}
```

## Setup and Usage

1. **Generate sample data:**
   ```bash
   python generate_data.py
   ```

2. **Generate monthly report:**
   ```bash
   python report.py database.csv april
   ```

3. **Available months:** january, february, march, april, may, june, july, august, september, october, november, december

## Requirements

- Python 3.x
- Standard Python libraries (csv, datetime, random)

## How It Works

### Data Generation
- Creates realistic employee records with random names and departments
- Generates hire dates within the last 10 years
- Creates birthdays with random months and days
- Writes data to CSV format for easy processing

### Report Generation
- Reads employee data from CSV file
- Identifies employees with birthdays in the specified month
- Identifies employees with hiring anniversaries in the specified month
- Groups results by department
- Calculates totals for each category

## Benefits

- **Time Savings**: Eliminates manual searching through paper archives
- **Accuracy**: Reduces human error in data collection
- **Cost Efficiency**: Enables bulk purchasing of gifts with better planning
- **Scalability**: Easily handles large employee databases
- **Automation**: Can be scheduled for monthly execution

## Customization

To modify the system:
1. Edit `generate_data.py` to change number of employees or data fields
2. Modify `report.py` to change how anniversaries are calculated
3. Adjust department names in either file as needed

