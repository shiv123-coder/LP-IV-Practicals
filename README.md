# Laboratory Practice - IV (LP-IV) Practicals 💻🛡️

[![GitHub repo](https://img.shields.io/badge/GitHub-LP--IV--Practicals-181717?style=flat&logo=github)](https://github.com/shiv123-coder/LP-IV-Practicals)
[![Course](https://img.shields.io/badge/SPPU_Course-410257_(LP--IV)-blue.svg)]()
[![Degree](https://img.shields.io/badge/Degree-B.E._Computer_Engineering-navy.svg)]()
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Java](https://img.shields.io/badge/Java-11%2B-ED8B00?logo=openjdk&logoColor=white)](https://www.java.com/)
[![PHP](https://img.shields.io/badge/PHP-8%2B-777BB4?logo=php&logoColor=white)](https://www.php.net/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0%2B-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)

Comprehensive laboratory practicals, assignments, documentation reports, and mini projects for **Laboratory Practice - IV (LP-IV)**, curriculum prescribed by **Savitribai Phule Pune University (SPPU)** for Final Year (Semester VII) Bachelor of Engineering (B.E.) in Computer Engineering (2019 Pattern).

---

## 📌 Student & Academic Profile

| Field | Details |
| :--- | :--- |
| **Student Name** | Shivshankar Mali |
| **Roll Number** | 49 |
| **Division** | C |
| **Academic Year** | 2026 – 2027 |
| **Semester** | Semester VII (B.E. Computer Engineering) |
| **Course Name** | Laboratory Practice - IV (LP-IV) |
| **Course Code** | 410257 |
| **Subjects Covered** | 1. Cyber Security and Digital Forensics (CSDF)<br>2. Software Testing and Quality Assurance (STQA) |
| **Institute** | JSPM's Bhivarabai Sawant Institute of Technology and Research (BSIOTR), Wagholi, Pune |
| **Affiliation** | Savitribai Phule Pune University (SPPU) |

---

## 📁 Repository Directory Structure

```
07_LP-IV_Laboratory_Practice_IV/
│
├── 01_CSDF/                                                # Cyber Security & Digital Forensics
│   ├── 01_Email_Tracking_and_Header_Analysis/             # Assignment 1: Email forensics & hop analysis
│   │   ├── email_header_analyzer.py                        # Header parser & hop IP extractor
│   │   ├── sample_header.txt                               # Sample RFC 822 email header
│   │   ├── CSDF1.pdf                                       # Practical write-up & lab report
│   │   └── assignment-1-mail-server-analyzer-1(CSDF 1).pdf# Reference problem statement
│   │
│   ├── 02_CAPTCHA_Generation_and_Verification/             # Assignment 2: Security & bot prevention
│   │   ├── captcha_generator.py                            # ImageCaptcha generator & validator
│   │   ├── captcha.png                                     # Generated visual challenge sample
│   │   ├── CSDF2 .pdf                                      # Practical report
│   │   └── assignment-2-captcha-1(CSDF 2).pdf              # Assignment problem definition
│   │
│   ├── 03_Recovering_Deleted_Files_and_Partitions/         # Assignment 3: Data carving & recovery
│   │   ├── recover.py                                      # Metadata & trash record recovery engine
│   │   ├── Documents/                                      # Recovered file targets (marks.csv, report.txt, test.py)
│   │   ├── CSDF3.pdf                                       # Practical report & output
│   │   └── assignment-3-data-recovery-2(CSDF 4).pdf        # Assignment guide
│   │
│   ├── 04_Log_Capturing_and_Event_Correlation/             # Assignment 4: SIEM log analysis
│   │   ├── log_correlate.py                                # Squid/Apache log correlation engine
│   │   ├── access.log                                      # Sample server proxy access log
│   │   ├── CSDF4.pdf                                       # Practical report & correlation summary
│   │   └── assignment-4-log-captuering-1(CSDF 5).pdf       # Problem statement
│   │
│   ├── 05_Study_and_Implementation_of_Honeypot/            # Assignment 5: Threat deception
│   │   ├── honeypot.py                                     # Multi-port socket honeypot (FTP, Telnet, HTTP)
│   │   ├── honeypot.log                                    # Real-time attacker interaction log
│   │   ├── CSDF5.pdf                                       # Practical report
│   │   └── group-a-5-honeypot-1(CSDF 7).pdf                # Manual documentation
│   │
│   └── 06_Mini_Project/                                    # CSDF Mini Project: Image Forensics Tool
│       ├── app.py                                          # Full Tkinter GUI forensics application
│       ├── requirements.txt                                # Python dependencies (Pillow)
│       ├── test_image_forensics.jpg                        # Test evidence image
│       ├── main.tex                                        # Academic LaTeX project report
│       ├── Mini_Project_Report.pdf                         # Technical project report
│       ├── 1.png                                           # GUI metadata inspection screenshot
│       ├── 2.png                                           # Error Level Analysis (ELA) screenshot
│       └── README.md                                       # Dedicated mini project documentation
│
└── 02_STQA/                                                # Software Testing & Quality Assurance
    ├── STQA_Manual_BSIOTR.pdf                              # Department lab manual & guidelines
    ├── 01_Test_Scenario_for_Gmail_Login_Page/              # Assignment 1: Test scenarios for Gmail login
    │   └── STQA1.pdf                                       # Scenario design, BVA & equivalence partitioning
    │
    ├── 02_Test_Scenario_for_Gmail_Inbox_Functionality/     # Assignment 2: Inbox functional scenarios
    │   └── STQA2.pdf                                       # Search, compose, label & filter scenarios
    │
    ├── 03_Test_Cases_for_Social_Media_Application/         # Assignment 3: Social media test suites
    │   └── STQA3.pdf                                       # End-to-end test cases (feed, profile, security)
    │
    ├── 04_Defect_Report_for_Application/                   # Assignment 4: Defect logging & tracking
    │   └── STQA4.pdf                                       # IEEE 829 defect report & bug lifecycle
    │
    ├── 05_Installation_of_Selenium_Grid_and_WebDriver/     # Assignment 5: Automated web testing
    │   ├── FirstTest.java                                  # Selenium WebDriver Chrome automation script
    │   └── STQA5.pdf                                       # Installation steps, Grid architecture & execution
    │
    └── 06_Mini_Project_COVID19_Information_Website/        # STQA Mini Project: Web App Testing
        ├── index.php                                       # Dynamic homepage & public guidance
        ├── login.php                                       # User authentication portal
        ├── register.php                                    # Registration with server-side validation
        ├── logout.php                                      # Session termination script
        ├── config.php                                      # MySQL database connection configuration
        ├── database.sql                                    # Database schema & initial tables
        ├── style.css                                       # Responsive stylesheets
        ├── script.js                                       # Client-side input validation scripts
        ├── regex_test_cases.md                             # Regex validation test suite & test results
        ├── Mini_Project_Report.pdf                         # Comprehensive technical report
        ├── 01_Home_Page.png                                # Screenshot: Public awareness portal
        ├── 02_COVID19_Information_and_Symptoms.png         # Screenshot: Symptoms advisory interface
        ├── 03_User_Login_Page.png                          # Screenshot: Authentication form
        ├── 04_Logged_In_User_Shivshankar_Mali.png          # Screenshot: Authenticated session state
        └── README.md                                       # STQA mini project setup & execution guide
```

---

## 🛡️ Module 1: Cyber Security and Digital Forensics (CSDF)

The **CSDF** component focuses on defensive controls, threat interception, evidence acquisition, log analysis, and file tampering detection.

### Summary Table

| Assignment | Title | Source / Script | Report PDF | Key Concepts / Techniques |
| :---: | :--- | :--- | :--- | :--- |
| **01** | Email Tracking and Header Analysis | [`email_header_analyzer.py`](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/01_Email_Tracking_and_Header_Analysis/email_header_analyzer.py) | [CSDF1.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/01_Email_Tracking_and_Header_Analysis/CSDF1.pdf) | Parsing RFC 822 `Received` headers, extracting originating IP addresses, tracing relay hops, verifying SPF/DKIM/DMARC headers. |
| **02** | CAPTCHA Generation and Verification | [`captcha_generator.py`](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/02_CAPTCHA_Generation_and_Verification/captcha_generator.py) | [CSDF2 .pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/02_CAPTCHA_Generation_and_Verification/CSDF2%20.pdf) | Automated challenge-response security, generating visual noise and distortions with `ImageCaptcha`, case-insensitive input verification. |
| **03** | Recovering Deleted Files and Partitions | [`recover.py`](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/03_Recovering_Deleted_Files_and_Partitions/recover.py) | [CSDF3.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/03_Recovering_Deleted_Files_and_Partitions/CSDF3.pdf) | Digital data preservation, FreeDesktop trash specifications, metadata restoration from `.trashinfo`, file carving principles. |
| **04** | Log Capturing and Event Correlation | [`log_correlate.py`](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/04_Log_Capturing_and_Event_Correlation/log_correlate.py) | [CSDF4.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/04_Log_Capturing_and_Event_Correlation/CSDF4.pdf) | Parsing proxy/firewall access logs, calculating client bandwidth consumption, detecting HTTP 407 authentication brute forcing, high-volume download detection. |
| **05** | Study and Implementation of Honeypot | [`honeypot.py`](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/05_Study_and_Implementation_of_Honeypot/honeypot.py) | [CSDF5.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/05_Study_and_Implementation_of_Honeypot/CSDF5.pdf) | Low-interaction deception sockets on ports 2121 (FTP), 2323 (Telnet), and 8081 (HTTP); multi-threaded attacker connection logging. |
| **06** | **Mini Project: Image Forensics Tool** | [`app.py`](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/06_Mini_Project/app.py) | [Report.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/01_CSDF/06_Mini_Project/Mini_Project_Report.pdf) | Desktop GUI (Tkinter) for cryptographic SHA-256 evidence hashing, deep EXIF metadata extraction, and Error Level Analysis (ELA) with $15\times$ amplification. |

---

## 🧪 Module 2: Software Testing and Quality Assurance (STQA)

The **STQA** component covers quality management, verification, validation, test design techniques (black-box & white-box), automated testing frameworks, and defect reporting standards.

### Summary Table

| Assignment | Title | Source / Script | Report PDF | Key Concepts / Techniques |
| :---: | :--- | :--- | :--- | :--- |
| **01** | Test Scenario for Gmail Login Page | Test Suite Document | [STQA1.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/02_STQA/01_Test_Scenario_for_Gmail_Login_Page/STQA1.pdf) | Positive & negative test scenario design, Boundary Value Analysis (BVA), Equivalence Class Partitioning (ECP), validation messages. |
| **02** | Test Scenario for Gmail Inbox Functionality | Test Suite Document | [STQA2.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/02_STQA/02_Test_Scenario_for_Gmail_Inbox_Functionality/STQA2.pdf) | Functional testing of search queries, label categorization, draft autosaving, star/flag toggling, bulk archiving, pagination. |
| **03** | Test Cases for Social Media Application | Test Matrix | [STQA3.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/02_STQA/03_Test_Cases_for_Social_Media_Application/STQA3.pdf) | Functional, UI, responsiveness, security, and session management test cases covering feed updates, likes, commenting, user permissions. |
| **04** | Defect Report for Application | Defect Tracking Sheet | [STQA4.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/02_STQA/04_Defect_Report_for_Application/STQA4.pdf) | Standard IEEE 829 defect reporting format: Defect ID, Severity, Priority, Steps to Reproduce, Expected vs Actual Behavior, Defect Life Cycle. |
| **05** | Installation of Selenium Grid and WebDriver | [`FirstTest.java`](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/02_STQA/05_Installation_of_Selenium_Grid_and_WebDriver/FirstTest.java) | [STQA5.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/02_STQA/05_Installation_of_Selenium_Grid_and_WebDriver/STQA5.pdf) | Selenium Hub & Node distributed architecture, standalone server configuration, automated ChromeDriver browser control in Java. |
| **06** | **Mini Project: COVID-19 Information Website** | PHP & MySQL Application | [Report.pdf](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/02_STQA/06_Mini_Project_COVID19_Information_Website/Mini_Project_Report.pdf) | Dynamic web application featuring client/server regular expression validation, password hashing, session management, and test documentation ([`regex_test_cases.md`](file:///d:/~BE_CSE_2026-27_Sem_7/07_LP-IV_Laboratory_Practice_IV/02_STQA/06_Mini_Project_COVID19_Information_Website/regex_test_cases.md)). |

---

## 🚀 Execution & Setup Instructions

### 1. Running CSDF Python Practicals

#### Environment Setup:
```powershell
# Open terminal in repository root
cd d:\~BE_CSE_2026-27_Sem_7\07_LP-IV_Laboratory_Practice_IV

# Create and activate Python virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install Pillow and Captcha dependencies
pip install pillow captcha
```

#### Running Assignments:
- **Assignment 1 (Email Header Analysis):**
  ```powershell
  python .\01_CSDF\01_Email_Tracking_and_Header_Analysis\email_header_analyzer.py
  ```
- **Assignment 2 (CAPTCHA Generation):**
  ```powershell
  python .\01_CSDF\02_CAPTCHA_Generation_and_Verification\captcha_generator.py
  ```
- **Assignment 3 (File Recovery):**
  ```powershell
  python .\01_CSDF\03_Recovering_Deleted_Files_and_Partitions\recover.py
  ```
- **Assignment 4 (Log Correlation):**
  ```powershell
  python .\01_CSDF\04_Log_Capturing_and_Event_Correlation\log_correlate.py
  ```
- **Assignment 5 (Honeypot):**
  ```powershell
  python .\01_CSDF\05_Study_and_Implementation_of_Honeypot\honeypot.py
  ```
- **Mini Project (Image Forensics Tool):**
  ```powershell
  python .\01_CSDF\06_Mini_Project\app.py
  ```

---

### 2. Running STQA Practicals

#### Selenium WebDriver (Assignment 5):
1. Ensure Java Development Kit (JDK 11+) and ChromeDriver matching your Google Chrome version are installed.
2. Compile and run `FirstTest.java`:
   ```powershell
   javac -cp ".;selenium-server-standalone.jar" .\02_STQA\05_Installation_of_Selenium_Grid_and_WebDriver\FirstTest.java
   java -cp ".;selenium-server-standalone.jar" demo.FirstTest
   ```

#### COVID-19 Website Mini Project (Assignment 6):
1. Install [XAMPP](https://www.apachefriends.org/) (PHP 8.0+ and MySQL).
2. Copy `02_STQA/06_Mini_Project_COVID19_Information_Website` to `C:\xampp\htdocs\covid19_info_website`.
3. Open `http://localhost/phpmyadmin`, create a database `covid19_info`, and import `database.sql`.
4. Access the web application at: `http://localhost/covid19_info_website/`.

---

## 📜 Academic Integrity & Disclaimer

This repository contains academic laboratory practical submissions, source implementations, and technical documentation prepared by **Shivshankar Mali** in partial fulfillment of the requirements for the **B.E. Computer Engineering** degree under **Savitribai Phule Pune University (SPPU)**.

The contents are organized for educational reference, academic archival, and knowledge sharing.
