
import requests
from urllib.parse import urlparse

SECURITY_HEADERS = {
    "Strict-Transport-Security": "Enforces HTTPS",
    "Content-Security-Policy": "Helps prevent XSS",
    "X-Content-Type-Options": "Prevents MIME sniffing",
    "X-Frame-Options": "Helps prevent clickjacking",
    "Referrer-Policy": "Controls referrer information",
}

def scan_website(url):
    parsed = urlparse(url)

    if parsed.scheme != "https" or not parsed.netloc:
        print("Please enter a valid HTTPS URL.")
        return

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        print("\nWebsite Security Header Scan")
        print("-" * 35)
        print("URL:", response.url)
        print("HTTP Status:", response.status_code)

        for header, purpose in SECURITY_HEADERS.items():
            if header in response.headers:
                print(f"[PASS] {header}: Present")
            else:
                print(f"[CHECK] {header}: Missing")
                print("       Purpose:", purpose)

        print("\nScan completed.")

    except requests.RequestException as error:
        print("Unable to scan website:", error)

if __name__ == "__main__":
    website = input("Enter an HTTPS website URL: ").strip()
    scan_website(website)
