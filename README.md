# 🚀 BDD Login & Logout Automation

This repository contains two sibling projects that automate login and logout flows on [saucedemo.com](https://www.saucedemo.com), showcasing Behavior-Driven Development (BDD) with Java and Python.

![Java](https://img.shields.io/badge/Java-blue?logo=java&logoColor=white)
![Python](https://img.shields.io/badge/Python-Behave-blue?logo=python)
![Selenium](https://img.shields.io/badge/Tested%20With-Selenium-43B02A?logo=selenium)

---

## 📂 Projects

- [`cucumber-java/`](./cucumber-java)  
  💻 Java + Maven + Cucumber + Selenium + JUnit 5  
  Automates login and logout using feature files and step definitions in Java.

- [`behave-python/`](./behave-python)  
  🐍 Python + Behave + Selenium  
  BDD-style test scenarios for login/logout using Python.

Each folder contains its own `README.md` with:

- 🔧 Setup instructions  
- ▶️ Execution commands  
- 🧪 Test results overview

---

## 🧾 Features Covered

- ✅ Valid Login  
- ✅ Logout from homepage  
- ❌ Invalid Login attempts  
- ⚠️ Alert handling (if any)

---

## 📁 Project Structure

```text
bdd-login-logout-automation/
├── behave-python/               # Python project using Behave
│   ├── features/                # Feature files and step definitions
│   │   ├── steps/               # Python step implementations
│   │   └── login_logout.feature # BDD scenarios for login/logout
│   ├── environment.py           # Behave environment hooks (setup/teardown)
│   └── requirements.txt         # Python dependencies
│
├── cucumber-java/              # Java project using Cucumber
│   ├── src/
│   │   ├── main/
│   │   │   └── java/            # Page objects, utilities, etc.
│   │   └── test/
│   │       ├── java/           # Step definitions, test runner
│   │       └── resources/
│   │           └── features/   # .feature files
│   └── pom.xml                 # Maven configuration
│
├── .gitignore
└── README.md                   # Project overview



