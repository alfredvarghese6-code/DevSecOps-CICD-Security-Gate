
# Project Report
## Website Security Scanner Using Python

### 1. Introduction
Website security is important for protecting users and web applications. HTTP security headers help reduce certain web security risks.

### 2. Objective
The objective is to develop a Python tool that checks important HTTP security headers and reports missing protections.

### 3. Tools and Technologies
- Python
- Requests library
- HTTP and HTTPS
- Visual Studio Code or any Python editor

### 4. Methodology
The scanner accepts an HTTPS website URL and sends an HTTP request. It checks the response status and examines selected security headers. Missing headers are reported for further review.

### 5. Implementation
The project uses Python's Requests library to retrieve HTTP responses. The program checks five security headers: Strict-Transport-Security, Content-Security-Policy, X-Content-Type-Options, X-Frame-Options, and Referrer-Policy.

### 6. Expected Output
The program displays the website URL, HTTP status, and whether each selected security header is present or missing.

### 7. Advantages
- Simple and easy to use
- Automates basic security-header checks
- Helps identify missing security protections
- Useful for cybersecurity learning

### 8. Limitations
The scanner checks only selected HTTP security headers. A missing header does not automatically prove a website is vulnerable. The tool does not replace a professional security assessment.

### 9. Future Enhancements
Future versions could include HTML reports, additional security checks, and a graphical user interface.

### 10. Conclusion
The Website Security Scanner demonstrates how Python can automate basic website security checks and help developers review HTTP security headers.

### References
1. Python: https://www.python.org/
2. Requests Documentation: https://requests.readthedocs.io/
3. OWASP Secure Headers Project: https://owasp.org/www-project-secure-headers/
