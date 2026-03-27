# 🚀 Playwright SauceDemo Automation Framework

## 📌 Overview

This project demonstrates a **scalable UI automation framework** built using Playwright with Python.
It follows modern automation practices like **Page Object Model (POM)**, **Pytest fixtures**, and **data-driven testing**.

The framework automates real-world e-commerce scenarios on SauceDemo, including login validation and cart functionality.

---

## 🛠 Tech Stack

* Python 🐍
* Playwright 🎭
* Pytest ⚡
* GitHub (Version Control)

---

## 📂 Project Structure

```
playwright-saucedemo/
│
├── tests/                # Test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   └── conftest.py
│
├── pages/                # Page Object Model (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── utils/                # Config & utilities
│   └── config.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ✅ Features Implemented

### 🔐 Authentication Testing

* Valid login
* Invalid login
* Locked user validation

### 🛒 E-Commerce Flow

* Add item to cart
* Verify cart badge count
* Validate items in cart

### ⚙️ Framework Features

* Pytest fixtures for setup & teardown
* Data-driven testing using `@pytest.mark.parametrize`
* Page Object Model (POM) design pattern
* Centralized configuration management

---

## ▶️ How to Run

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd playwright-saucedemo
```

### 2. Setup environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Install browsers

```bash
playwright install
```

### 4. Run tests

```bash
pytest -v
```

---

## 🧠 Key Learnings

* Difference between Selenium and Playwright (auto-waiting, stability)
* Importance of clean test architecture (POM)
* Fixture-based test design in Pytest
* Data-driven testing for scalability
* Debugging real-world issues (env setup, imports, Git errors)

---

## 🚀 Future Enhancements

* ✅ Remove item from cart
* ✅ Checkout flow automation
* ⏳ API testing integration (Playwright request)
* ⏳ Allure reporting
* ⏳ Parallel execution
* ⏳ CI/CD using GitHub Actions

---

## 💡 Why This Project Stands Out

This is not just a script-based automation project —
it demonstrates **framework-level thinking** and **real-world test design**, aligning with SDET-level expectations.

---
