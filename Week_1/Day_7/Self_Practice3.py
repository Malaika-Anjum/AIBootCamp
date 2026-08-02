#Support command-line arguments for quicker task management

from datetime import datetime
import sys
import csv

if len(sys.argv) != 4:
    print("Usage: python Self_Practice3.py <title> <deadline> <priority>")
    print("Example: python Self_Practice3.py \"Study Numpy\" 2026-07-15 1")
    sys.exit(1)

title = sys.argv[1]
deadline = datetime.strptime(sys.argv[2], "%Y-%m-%d")
priority = int(sys.argv[3])

task = {
    "title": title,
    "deadline": deadline,
    "priority": priority
}

with open("tasks.csv", "a", newline="") as file:
    writer = csv.writer(file)

    # Write the header only if the file is empty.
    if file.tell() == 0:
        writer.writerow(["Title", "Priority", "Deadline"])

    writer.writerow([
        task["title"],
        task["priority"],
        task["deadline"].strftime("%Y-%m-%d")
    ])

print("Task saved to tasks.csv")