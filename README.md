
# Website Security Scanner

## Project Description
A Python-based Website Security Scanner that checks important HTTP security headers to identify missing security protections.

## Features
- Checks website HTTP status
- Detects missing security headers
- Checks HTTPS URLs
- Displays security scan results
- Handles connection errors

## Technologies Used
- Python
- Requests library
- HTTP Security Headers

## Installation
Install the required dependency:

```bash
pip install -r requirements.txt
```

## How to Run
Execute the following command:

```bash
python scanner.py
```

Enter an HTTPS website URL when prompted.

## Security Checks
The scanner checks:
- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy

## Limitations
This is a basic security-header checker. It does not perform a complete vulnerability assessment.

## Responsible Use
Scan only websites you own or have permission to test.
