#  Selenium E2E Test Automation Framework

![License](https://img.shields.io/badge/License-MIT-blue.svg)
This is an **End-to-End Test Automation Framework** built using **Python, Selenium, and Pytest**.  
It automates the testing of an e-commerce web application.

---

## 📂 Project Structure


```
selenium-ecommerce-automation/
│
├── config/ 
│
├── pages/ 
│ ├── login_page.py
│ ├── shop_page.py
│ └── checkout_page.py
│
├── reports/ 
│
├── tests/ 
│ ├── test_e2eTestFramework.py
│ └── conftest.py
│
├── utils/ 
│ ├── logger.py
│ └── read_config.py
│
├── requirements.txt 
├── README.md 
└── .gitignore 

```
---
## ✨ Features

- ✅ **Page Object Model (POM)** structure  
- ✅ **Cross-browser support** (Chrome, Edge)  
- ✅ **Headless mode** for CI/CD pipelines  
- ✅ **HTML Test Reports** using `pytest-html`  
- ✅ **Config-driven test data** (`config.json`)  
- ✅ **Logging support** for debugging 

---

## ⚙️ Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chandhu746/selenium-ecommerce-automation.git
   cd selenium-ecommerce-automation

2.**Create & Activate  Virtual Environment**

python -m venv .venv
## Windows
.venv\Scripts\activate
## Mac/Linux
source .venv/bin/activate

3.**Install dependencies**

pip install -r requirements.txt

Running Tests

##Run all Tests(default: Chrome)##

pytest test_name --browser_name(optional) 

##Run in Headless mode##

pytest tests/ --browser_name=chrome --headless --html=reports/report.html --self-contained-html

##Run in Edge##
pytest tests/ --browser_name=edge --html=reports/report.html --self-contained-html

##📊 Reports##

After execution, reports are generated in:

reports/report.html

## 📜 License

This project is licensed under the [MIT License](LICENSE).









