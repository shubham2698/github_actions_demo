import csv
from datetime import datetime

def get_data(file_path):
    today_date = datetime.now().strftime('%d/%m/%Y')
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['DATE']
            if row['DATE'] == today_date:
                return row['TASK']
