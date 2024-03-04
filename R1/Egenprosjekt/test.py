import csv
from datetime import datetime
import matplotlib.pyplot as plt

def process_data(data):
    total_cases = 0
    current_date = None
    dates = []
    cases = []

    for entry in data:
        date_str, cases_str = entry['date'], entry['cases']
        date = datetime.strptime(date_str, '%Y-%m-%d')

        if current_date is None:
            current_date = date
        elif date != current_date:
            dates.append(current_date)
            cases.append(total_cases)
            current_date = date

        total_cases += int(cases_str)

    return dates, cases

# Read data from CSV file
csv_file_path = r'R1\Egenprosjekt\data.csv'  # Replace with your actual CSV file path
data = []

with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append({'date': row['date'], 'cases': row['cases']})

dates, cases = process_data(data)

# Plotting
plt.plot(dates, cases, marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.title('COVID-19 Cases Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
