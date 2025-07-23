# detectors/enumeration.py

def detect_404_scan(log_line):
    if "404" in log_line and ("/admin" in log_line or "/login" in log_line or "/phpmyadmin" in log_line):
        return True
    return False
