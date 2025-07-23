# detectors/sql_injection.py

import re

def detect_sql_injection(log_line):
    patterns = [
        r"' OR 1=1", r"'--", r"union select", r"drop table", r" or ", r"--"
    ]
    for pattern in patterns:
        if re.search(pattern, log_line, re.IGNORECASE):
            return True
    return False
