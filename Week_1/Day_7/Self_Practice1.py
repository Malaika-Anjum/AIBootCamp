#Add deadlines or priorities for tasks

from datetime import datetime

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

tasks.sort(key=lambda t: (t["priority"], t["deadline"]))

print("\nTasks:")
for task in tasks:
    print(
        f"{task['title']} | "
        f"Priority: {task['priority']} | "
        f"Deadline: {task['deadline'].strftime('%Y-%m-%d')}"
    )