# Real-Time Log Threat Detector (SIEM-Lite v2)

## Overview

The Real-Time Log Threat Detector (SIEM-Lite v2) is a lightweight Security Information and Event Management (SIEM) tool built in Python. It continuously monitors log files in real time to detect suspicious activities such as unauthorized logins, repeated failed attempts, and other security-related events. This project simulates a Security Operations Center (SOC) analyst's workflow by analyzing logs, generating alerts, and helping improve incident response times.

## Features

- **Real-time log monitoring:** Continuously watches log files for new entries.  
- **Threat detection:** Identifies suspicious events such as multiple failed login attempts, unauthorized access, and unusual activities.  
- **Alert system:** Generates alerts immediately when threats are detected.  
- **Modular design:** Easily extendable with custom detection rules or integrations.  
- **Log generation script:** Simulates log entries for testing and demonstration purposes.

## Technologies Used

- Python 3.x  
- File system monitoring (`watchdog` or custom polling)  
- Regular expressions for log parsing  
- Modular Python scripts for clean code organization

## Getting Started

### Prerequisites

- Python 3.7 or higher  
- Required Python packages (install via pip):

```bash
pip install -r requirements.txt
