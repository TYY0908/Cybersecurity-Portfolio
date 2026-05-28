# Phishing URL Checker

## Overview

A beginner web security awareness tool that checks a URL for suspicious characteristics commonly found in phishing links.

## Features

- Detects IP-address based URLs
- Flags suspicious keywords
- Checks for unusually long URLs
- Warns about missing HTTPS
- Produces a simple risk rating

## Technologies Used

- Python
- urllib.parse
- re

## How to Run

```bash
python url_checker.py
```

## Learning Focus

This project shows how phishing indicators can be converted into rule-based detection logic. It is not a replacement for a professional URL reputation service.
