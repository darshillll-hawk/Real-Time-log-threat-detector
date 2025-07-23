import time
import random


log_entries = [
    "2025-07-23 22:00:01 Login failed for user root from IP 192.168.1.10",
    "2025-07-23 22:00:04 SQL error at /login.php?user=' OR 1=1--",
    "2025-07-23 22:00:10 404 Not Found /admin",
    "2025-07-23 22:00:30 Successful login from 172.16.0.2",
    "2025-07-23 22:01:00 Invalid password for admin from 10.0.0.3",
    "2025-07-23 22:01:10 404 Not Found /phpmyadmin",
    "2025-07-23 22:01:40 User logged out successfully",
    "2025-07-23 22:02:00 DROP TABLE users; --",
]

def write_log_line():
    with open("logs/sample.log", "a") as f:
        log = random.choice(log_entries)
        f.write(log + "\n")
        f.flush()  # <-- Flush immediately to disk
        print(f"[Log Written] {log}")

if __name__ == "__main__":
    while True:
        write_log_line()
        time.sleep(2)  # Wait 2 seconds before writing next log
# logs/generate_logs.py
# This script generates sample log entries for testing the log monitoring system.