# Security Log Analyzer

## Overview

A small SOC-style Python project that reads authentication logs and identifies failed login activity.

## Features

- Parses a sample authentication log
- Counts failed login attempts by IP address
- Highlights repeated failures
- Prints a short investigation summary

## Technologies Used

- Python
- re
- collections
- pathlib

## How to Run

```bash
python log_analyzer.py
```

To analyze a different log file:

```bash
python log_analyzer.py path/to/logfile.log
```

## Learning Focus

This project practices basic blue-team skills: reading logs, extracting indicators, counting suspicious behavior, and summarizing findings.
