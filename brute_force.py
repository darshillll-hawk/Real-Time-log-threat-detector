# detectors/brute_force.py

def detect_brute_force(log_line):
    keywords = ["Login failed", "authentication failed", "Invalid password"]
    for word in keywords:
        if word.lower() in log_line.lower():
            return True
    return False
