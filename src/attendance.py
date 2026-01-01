import csv
import os
from datetime import datetime

def mark_attendance(name):
    # Ensure data directory exists
    os.makedirs('../data', exist_ok=True)

    file_path = '../data/attendance.csv'
    file_exists = os.path.isfile(file_path)

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)

        # Write header only if file is new
        if not file_exists:
            writer.writerow(['Name', 'Date', 'Time'])

        now = datetime.now()
        writer.writerow([
            name,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ])

if __name__ == "__main__":
    student_name = input("Enter student name: ")
    mark_attendance(student_name)
    print("Attendance marked successfully.")
