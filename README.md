# Selenium Training Notes and Practice

This folder contains various practice scripts and notes created during Selenium automation training.  
The files cover multiple core Selenium concepts, PyTest usage, and Data Driven Testing (DDT).

The purpose of this section is to provide **hands-on examples of different automation techniques** rather than a single integrated framework.

---

# Project Structure
```
.
│ ddt_notes
│ generate_reports
│ pytest_notes
│ x.py
│
├── ddt
│ ├── read_excel.py
│ ├── register.py
│ ├── reg_testdata.xlsx
│ └── init.py
│
├── files
│ ├── candidates_kiit.xlsx
│ ├── css_selector.html
│ ├── demo.html
│ ├── loading.html
│ └── progressbar.html
│
├── locators_
│ ├── 1_id.py
│ ├── 2_css_selector.py
│ ├── 3_xpath.py
│ └── init.py
│
├── pytest_package
│ ├── test_basics.py
│ ├── test_fixtures.py
│ ├── test_markers.py
│ └── init.py
│
├── pytest_package2
│ ├── conftest.py
│ ├── reg_report.html
│ ├── test_login.py
│ ├── test_reg.py
│ └── assets
│ └── style.css
│
└── training
├── actionchains.py
├── alerts_.py
├── assert__.py
├── browser_methods.py
├── file_upload_download_popup.py
├── frames_.py
├── headless_execution.py
├── initialize_browsers.py
├── listboxes_dropdowns.py
├── reading_excel.py
├── shadow_dom__.py
├── synchronization_.py
├── webelement_methods.py
├── window_handling.py
└── init.py
```


---

# Folder Description

## ddt
Contains scripts demonstrating **Data Driven Testing** using Excel.

- `read_excel.py` – utility script for reading Excel data
- `register.py` – registration automation using Excel inputs
- `reg_testdata.xlsx` – test data used for automation

---

## files
Contains **supporting files used during practice**, including:

- HTML pages for testing Selenium locators
- Sample Excel datasets

Examples:

- `css_selector.html`
- `demo.html`
- `loading.html`
- `progressbar.html`

---

## locators_
Contains scripts demonstrating **different Selenium locator strategies**.

- ID locator
- CSS selector
- XPath

---

## pytest_package
Basic PyTest learning examples.

Includes:

- Test structure
- Fixtures
- Markers

Files:

- `test_basics.py`
- `test_fixtures.py`
- `test_markers.py`

---

## pytest_package2
Advanced PyTest usage including:

- `conftest.py` for shared fixtures
- Multiple test modules
- HTML report generation

Example files:

- `test_login.py`
- `test_reg.py`
- `reg_report.html`

---

## training
Contains scripts demonstrating **core Selenium automation concepts**, including:

- Browser initialization
- Web element methods
- Alerts handling
- Frames handling
- Window handling
- File upload/download
- Synchronization (waits)
- Shadow DOM interaction
- Action Chains
- Headless browser execution
- Dropdown and listbox handling

---

# Topics Covered

The training material covers the following Selenium topics:

- WebDriver initialization
- Web element methods
- Browser navigation methods
- Locator strategies (ID, CSS, XPath)
- Alerts handling
- Frames handling
- Window handling
- Dropdowns and listboxes
- File upload and download
- Action Chains
- Shadow DOM
- Synchronization techniques
- Headless execution
- Data Driven Testing (DDT)
- PyTest basics and advanced features
