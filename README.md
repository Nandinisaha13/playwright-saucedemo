# 🚀 Playwright SauceDemo Automation Framework

## 📌 Overview

This project demonstrates a **scalable UI automation framework** built using Playwright with Python.
It automates real-world e-commerce scenarios on SauceDemo using modern testing practices like **Page Object Model (POM)**, **Pytest fixtures**, and **CI/CD integration**.

---

## 🛠 Tech Stack

* Python 🐍
* Playwright 🎭
* Pytest ⚡
* GitHub Actions (CI/CD) 🔄

---

## 📂 Project Structure

```
playwright-saucedemo/
│
├── tests/                # Test cases
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_remove.py
│   ├── test_multipleitems.py
│   └── conftest.py
│
├── pages/                # Page Object Model (POM)
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── utils/                # Config & utilities
│   └── config.py
│
├── reports/              # HTML reports (generated)
├── screenshots/          # Failure screenshots
│
├── .github/workflows/    # CI/CD pipeline
│   └── tests.yml
│
├── README.md
├── .gitignore
```

---

## ✅ Features Implemented

### 🔐 Authentication Testing

* Valid login
* Invalid login
* Locked user validation

### 🛒 Cart Functionality

* Add single item
* Add multiple items dynamically
* Remove item from cart
* Validate cart count

### 🧠 Advanced Item Handling

* Add items by **product name (dynamic locator)**
* Avoid index-based selection
* Handle dynamic DOM updates

### 🛍️ Cart Validation

* Validate item names in cart
* Validate item prices
* Validate multiple items

### 💳 Checkout Flow

* Complete end-to-end checkout
* Form validation (positive & negative scenarios)
* Order confirmation validation

### 🔄 Sorting Validation

* Price: Low → High
* Price: High → Low
* UI data vs programmatic validation

### ⚙️ Framework Features

* Page Object Model (POM)
* Pytest fixtures (reusable setup)
* Data-driven testing (`@pytest.mark.parametrize`)
* Dynamic locator strategies
* Clean separation of concerns

---

## 📊 Reporting & Debugging

* HTML Test Reports (`pytest-html`)
* Screenshot capture on failure
* Clean separation of report and debug artifacts

---

## 🚀 CI/CD Integration

* GitHub Actions pipeline
* Automatic test execution on push
* Report & screenshot artifacts upload

---

## ▶️ How to Run Locally

### 1. Clone the repo

```
git clone https://github.com/Nandinisaha13/playwright-saucedemo.git
cd playwright-saucedemo
```

### 2. Setup environment

```
python -m venv venv
source venv/bin/activate
pip install pytest playwright pytest-html
playwright install
```

### 3. Run tests

```
pytest --html=reports/report.html
```

---

## 🧠 Key Learnings

* Handling dynamic DOM changes in UI automation
* Choosing stable locators (`data-test`, text-based)
* Avoiding flaky tests with Playwright auto-waiting
* Building reusable and scalable test frameworks
* Debugging CI/CD environment differences
* Managing Git and repository hygiene

---

## 🚀 Future Enhancements

* 🔜 Name-based sorting validation
* 🔜 Parallel test execution
* 🔜 API + UI integration (Playwright request)
* 🔜 Allure reporting

---

## 💡 Why This Project Stands Out

This project demonstrates:

* Real-world test scenarios (not just demo scripts)
* Strong framework design principles
* Debugging and problem-solving skills
* CI/CD readiness



