#Add deadlines or priorities for tasks
# #Export tasks to a JSON or CSV file

from datetime import datetime
import csv


tasks = []

while True:
    title = input("Task name (or 'quit' to stop): ")
    if title.lower() == "quit":
        break

    deadline = input("Deadline (YYYY-MM-DD): ")
    priority = int(input("Priority (1 = highest): "))

    tasks.append({
        "title": title,
        "deadline": datetime.strptime(deadline, "%Y-%m-%d"),
        "priority": priority
    })

with open("tasks.csv", "w") as file:
    file.write("Title,Priority,Deadline\n")  # header row

    for task in tasks:
        file.write(
            f"{task['title']},{task['priority']},"
            f"{task['deadline'].strftime('%Y-%m-%d')}\n"
        )

print("Tasks saved to tasks.csv")