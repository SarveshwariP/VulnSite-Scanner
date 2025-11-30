# Log Analysis & Threat Detection using Splunk / ELK Stack + Vulnerability Scanner

This project contains:

- A Log Analysis project using **Splunk / ELK Stack**  
- A custom-built **Python Vulnerability Scanner**  
- Basic vulnerable PHP pages for demonstration  
- Detection of common web vulnerabilities  

---

## 🎯 OBJECTIVES

- Collect & ingest sample system/web logs  
- Analyze logs for suspicious activities  
- Identify brute-force attacks, SQL injections, anomalies  
- Build dashboards & alerts  
- Generate SOC-style reports  
- Demonstrate vulnerability scanning  

---

## 🧱 PROJECT ARCHITECTURE
Log Source (Apache/MySQL/Linux)
        ↓
  Splunk / Logstash
        ↓
ElasticSearch (Index)
        ↓
Kibana / Splunk Dashboards
## 🛡️ Vulnerability Scanner (Python)

This scanner checks common web vulnerabilities like:
- SQL Injection
- XSS
- Open Redirect
- Command Injection

### 🔹 How to run the scanner
python scanner.py

## 📁 Project Folder Structure

VulnSite-Scanner/
│── scanner.py
│── vulnerable/
│      ├── login.php
│      ├── search.php
│── sample-logs/
│── README.md
## 🚀 How to Run

### 1. Run vulnerability scanner
python scanner.py

### 2. View vulnerable pages
Open the "vulnerable" folder → run using XAMPP or local PHP server.

### 3. Log Analysis
Import sample logs into:
- Splunk
or
- ELK Stack (Logstash → Elastisearch → Kibana dashboards)

