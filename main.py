# main.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

from detectors.brute_force import detect_brute_force
from detectors.sql_injection import detect_sql_injection
from detectors.enumeration import detect_404_scan

LOG_FILE = "logs/sample.log"

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(LOG_FILE):
            with open(LOG_FILE, "r") as file:
                lines = file.readlines()
                last_line = lines[-1].strip()
                print(f"[+] New Log Entry: {last_line}")
                analyze_log(last_line)

def analyze_log(log):
    if detect_brute_force(log):
        print("[!] Brute-force login attempt detected")
    elif detect_sql_injection(log):
        print("[!] Possible SQL injection detected")
    elif detect_404_scan(log):
        print("[!] 404 scan/enumeration detected")

if __name__ == "__main__":
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path="logs", recursive=False)
    observer.start()
    print(f"[+] Watching log file: {LOG_FILE}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
