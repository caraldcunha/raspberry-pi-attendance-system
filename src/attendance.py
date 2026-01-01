import csv
from datetime import datetime

def mark_attendance(name):
    now = datetime.now()
    with open('../data/attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S")])

if __name__ == "__main__":
    student_name = input("Enter student name: ")
    mark_attendance(student_name)
    print("Attendance marked successfully.")

