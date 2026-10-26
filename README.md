# 🛡️ Cybersecurity Awareness & Phishing Detection Platform

### An Interactive Cybersecurity Awareness and Phishing Detection System Built with Python, Streamlit, and SQLite

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![SQLite](https://img.shields.io/badge/Database-SQLite-green)
![Pytest](https://img.shields.io/badge/Testing-Pytest-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey)

---

## 📌 Project Overview

The **Cybersecurity Awareness & Phishing Detection Platform** is an educational cybersecurity application designed to help users understand phishing threats, evaluate suspicious URLs and emails, assess password strength, and improve cybersecurity awareness.

The project combines multiple cybersecurity modules into a single interactive dashboard.

It demonstrates practical Python programming, security analysis, database management, automated testing, and interactive data visualization.

### 🎯 Project Objectives

- Improve cybersecurity awareness.
- Identify common phishing indicators.
- Analyze potentially suspicious URLs.
- Detect suspicious patterns in email messages.
- Evaluate password strength.
- Provide interactive cybersecurity training.
- Store quiz results in an SQLite database.
- Visualize cybersecurity awareness statistics.
- Generate downloadable CSV reports.
- Demonstrate software testing and secure development practices.

---

## 🚀 Key Features

### 🔗 1. Phishing URL Analyzer

Analyzes URLs using rule-based security checks.

**Detection Indicators:**
- HTTP usage
- Suspicious keywords
- IP-based hostnames
- Unusually long URLs
- Excessive subdomains
- Suspicious URL structures
- Special characters and unusual patterns

**Output:**
- URL risk score
- Risk classification
- Security findings
- Potential phishing indicators

**Risk Levels:**
- 🟢 LOW
- 🟠 MEDIUM
- 🔴 HIGH

### 📧 2. Phishing Email Analyzer

Analyzes email content to identify common social engineering indicators.

**Detection Indicators:**
- Urgent action requests
- Suspicious phrases
- Password or account verification requests
- Requests for sensitive information
- Links within email content
- Potential phishing language

**Output:**
- Email risk score
- Risk classification
- Suspicious findings
- Extracted links

### 🔐 3. Password Strength Checker

Evaluates the estimated strength of test passwords.

**Security Checks:**
- Password length
- Uppercase characters
- Lowercase characters
- Numbers
- Special characters
- Common password patterns
- Repeated characters

**Output:**
- Password strength score
- Strength classification
- Improvement recommendations

**Privacy:** Passwords are not stored in the SQLite database.

### 🧠 4. Cybersecurity Awareness Quiz

An interactive quiz containing 10 cybersecurity awareness questions.

**Topics Covered:**
- Phishing attacks
- Password security
- Multi-factor authentication
- Suspicious emails
- HTTPS
- Ransomware
- Least privilege
- Software updates
- Social engineering
- Incident reporting

**Quiz Features:**
- Multiple-choice questions
- Automatic scoring
- Awareness level classification
- SQLite result storage

**Awareness Levels:**

| Score | Awareness Level |
|---|---|
| 0–49% | BEGINNER |
| 50–79% | INTERMEDIATE |
| 80–100% | ADVANCED |

### 🗄️ 5. SQLite Database

Stores cybersecurity awareness quiz results.

**Stored Information:**
- Quiz result ID
- Display name
- Quiz score
- Correct answers
- Total questions
- Awareness level
- Completion timestamp

The database is created automatically when the application starts.

### 📊 6. Security Awareness Dashboard

An interactive Streamlit dashboard that displays:

- Total completed quizzes
- Average quiz score
- Number of advanced results
- Cybersecurity awareness statistics
- Awareness level distribution
- Quiz history

### 📥 7. CSV Report Generation

Users can export quiz history into a CSV file for further analysis.

**Report Filename:**

`awareness_quiz_report.csv`

### 🧪 8. Automated Testing

The project includes automated tests using Pytest.

**Test Coverage Areas:**
- URL phishing detection
- Email phishing analysis
- Password strength checking
- Quiz scoring
- SQLite database operations

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web dashboard |
| Pandas | Data processing |
| Plotly | Interactive data visualization |
| SQLite | Local database |
| Pytest | Automated testing |
| Git | Version control |
| GitHub | Source code hosting |
| VS Code | Development environment |
| Windows 11 | Development operating system |

---

## 🏗️ System Architecture

```text
                    USER
                     |
                     v
             STREAMLIT DASHBOARD
                     |
        +------------+------------+
        |            |            |
        v            v            v
   URL ANALYZER  EMAIL ANALYZER  PASSWORD CHECKER
        |            |            |
        +------------+------------+
                     |
                     v
              SECURITY RESULTS

                     USER
                      |
                      v
              AWARENESS QUIZ
                      |
                      v
               QUIZ SCORING
                      |
                      v
               SQLITE DATABASE
                      |
                      v
              QUIZ HISTORY
                      |
                      v
              CSV REPORTING
```

---

## 📂 Project Structure

```text
Cybersecurity-Awareness-Phishing-Detection/
│
├── app.py
├── phishing_detector.py
├── email_analyzer.py
├── password_checker.py
├── quiz.py
├── database.py
│
├── data/
│   └── .gitkeep
│
├── reports/
│   └── .gitkeep
│
├── screenshots/
│   ├── overview.png
│   ├── url-analyzer.png
│   ├── email-analyzer.png
│   ├── password-checker.png
│   ├── awareness-quiz.png
│   ├── quiz-history.png
│   └── reports.png
│
├── tests/
│   ├── test_phishing.py
│   ├── test_email.py
│   ├── test_password.py
│   ├── test_quiz.py
│   └── test_database.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation Guide

### Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Cybersecurity-Awareness-Phishing-Detection.git
```

### Step 2 — Open the Project Folder

```bash
cd Cybersecurity-Awareness-Phishing-Detection
```

### Step 3 — Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4 — Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

### Step 5 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6 — Run the Application

```bash
python -m streamlit run app.py
```

### Step 7 — Open the Dashboard

Open the local Streamlit address displayed in the terminal.

Default address:

`http://localhost:8501`

---

## 📸 Project Screenshots

### 🛡️ 1. Overview Dashboard

The main dashboard displays cybersecurity modules and awareness statistics.

![Overview Dashboard]<img width="1875" height="903" alt="Screenshot_27-10-2026_32834_localhost" src="https://github.com/user-attachments/assets/1b0588f6-6b71-49a8-9aed-76665df43bc0" />


---

### 🔗 2. Phishing URL Analyzer

Analyze suspicious URLs and identify potential phishing indicators.

![Phishing URL Analyzer]<img width="1890" height="907" alt="Screenshot_27-10-2026_31859_localhost" src="https://github.com/user-attachments/assets/ab269c9f-5992-4407-aa70-07130471dac5" />


---

### 📧 3. Phishing Email Analyzer

Detect suspicious email content and potential social engineering indicators.

![Phishing Email Analyzer]<img width="1882" height="903" alt="Screenshot_27-10-2026_31948_localhost" src="https://github.com/user-attachments/assets/a67287b1-641d-4726-b17c-62e0975d5111" />


---

### 🔐 4. Password Strength Checker

Estimate password strength and receive security recommendations.

![Password Strength Checker]<img width="1886" height="906" alt="Screenshot_27-10-2026_31959_localhost" src="https://github.com/user-attachments/assets/53736842-25aa-4c8a-95e6-565b6a85f79b" />


---

### 🧠 5. Cybersecurity Awareness Quiz

Test cybersecurity knowledge through interactive multiple-choice questions.

![Cybersecurity Awareness Quiz]<img width="1886" height="905" alt="Screenshot_27-10-2026_32011_localhost" src="https://github.com/user-attachments/assets/a99bd2da-97d9-45b6-b678-98108f744f67" />


---

### 📊 6. Quiz History Dashboard

View saved quiz results and cybersecurity awareness statistics.

![Quiz History<img width="1892" height="906" alt="Screenshot_27-10-2026_32024_localhost" src="https://github.com/user-attachments/assets/4744d308-1867-4cc1-b00e-b87d38724ac4" />


---

### 📥 7. Security Reports

Export quiz history as a downloadable CSV report.

![Security Reports]<img width="1887" height="904" alt="Screenshot_27-10-2026_32036_localhost" src="https://github.com/user-attachments/assets/662d2e39-360b-4642-8b26-b3a341c1820a" />


---

## 🧪 Automated Testing

Automated tests are implemented using Pytest.

### Run All Tests

```bash
python -m pytest -v
```

### Test Modules

| Test File | Description |
|---|---|
| `test_phishing.py` | URL phishing detection tests |
| `test_email.py` | Email analysis tests |
| `test_password.py` | Password strength tests |
| `test_quiz.py` | Quiz scoring tests |
| `test_database.py` | SQLite database tests |

**Expected result for the current project version:**

```text
20 passed
```

---

## 🗄️ Database Design

**Database:** SQLite

**Database File:**

```text
data/awareness.db
```

**Table:** `quiz_results`

| Column | Description |
|---|---|
| id | Unique result identifier |
| username | Quiz participant display name |
| score | Quiz percentage |
| correct_answers | Number of correct answers |
| total_questions | Total quiz questions |
| awareness_level | Beginner, Intermediate, or Advanced |
| completed_at | Completion timestamp |

The database file is excluded from Git version control.

---

## 🔒 Security Considerations

The project follows basic security and privacy practices.

- Passwords are not stored in the database.
- Database operations use parameterized SQL queries.
- Virtual environment files are excluded from Git.
- Local database files are excluded from Git.
- Secret configuration files are excluded from Git.
- Suspicious URLs are analyzed without automatically visiting them.
- Security analysis is performed using educational heuristics.

**Important:** A LOW risk result does not guarantee that a URL or email is safe. Password strength scores are estimates, not guarantees.

---

## 🏆 Related Certification

### Fortinet — NSE 1 / Information Security Awareness

**Certification Provider:** Fortinet

**Related Skills:**
- Cybersecurity fundamentals
- Information security awareness
- Phishing awareness
- Social engineering awareness
- Password security
- Security best practices

**🔗 Badge Verification:**

[Verify My Fortinet Badge] https://www.credly.com/badges/f335269d-6b52-4374-bd2d-551532955f56/public_url

This project is an independent educational portfolio project inspired by cybersecurity awareness concepts. It is not an official Fortinet product or certification assessment.

---

## 💡 Skills Demonstrated

This project demonstrates practical knowledge in:

- Python development
- Cybersecurity fundamentals
- Phishing detection techniques
- Email security awareness
- Password security
- Security awareness training
- Streamlit application development
- SQLite database management
- Data visualization
- Automated software testing
- Git and GitHub
- Technical documentation

---

## 🔮 Future Improvements

Planned improvements include:

- Machine learning-based phishing detection
- URL reputation API integration
- More advanced email analysis
- User authentication
- Role-based access control
- Randomized cybersecurity quizzes
- Expanded question bank
- PDF report generation
- GitHub Actions CI/CD
- Advanced security analytics

---

## ⚠️ Disclaimer

This application is developed for **educational and cybersecurity awareness purposes only**.

It should not be used as a replacement for professional cybersecurity tools.

The detection modules use rule-based analysis and may produce false positives or false negatives.

Do not enter real passwords, confidential emails, or sensitive personal information into the demonstration application.

---

## 📌 Project Status

**Status:** Completed Educational Prototype

**Category:** Cybersecurity / Security Awareness / Phishing Detection

**Development Environment:** Windows 11

**Primary Language:** Python

---

## ⭐ Support

If you find this educational project useful, consider giving the repository a ⭐ on GitHub.

**Built for cybersecurity learning, awareness, and practical skill development.**
