# Write a program to log messages with timestamps into a file

from datetime import datetime

def log_message(filename, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as file:
        file.write(f"[{timestamp}] {message}\n")


messages = input("Enter messages to log :\n")

log_message("log.txt", messages)

print("Messages have been logged to log.txt")

