# INVU Registration Automation Project

This project automates the INVU registration flow using Selenium and Pytest.
It is structured as a small real-world QA automation project instead of a single script.

## Project structure

```
invu_registration_automation_project/
├── pages/
│   ├── base_page.py
│   └── registration_page.py
├── tests/
│   └── test_registration.py
├── utils/
│   ├── config.py
│   └── driver_factory.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── run_registration.py
```

## What this project covers

- Opens the INVU website
- Navigates to the login page
- Opens the registration form
- Fills in first name, last name, email, password, and confirm password
- Uses multiple fallback locators for better resilience
- Generates a unique email address automatically
- Supports optional form submission through environment variables
- Verifies post-submit behavior using URL and page content checks

## Technologies

- Python
- Selenium WebDriver
- Pytest
- WebDriver Manager

## Setup

1. Create and activate a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` values into your environment or set them manually.

## Run as a simple script

```bash
python run_registration.py
```

This opens the registration form and fills it.
By default, submission is disabled to avoid creating real accounts accidentally.

## Run tests with Pytest

```bash
pytest
```

## Run the real submission test

### Windows PowerShell

```powershell
$env:INVU_SUBMIT_FORM="true"
pytest -m optional_submission
```

### macOS / Linux

```bash
export INVU_SUBMIT_FORM=true
pytest -m optional_submission
```

## Important note

This project is best presented on GitHub as a **registration automation project**, not as a login automation project.
The script interacts with the registration form and can optionally submit it.

## Suggested GitHub description

"Automated INVU registration flow using Python, Selenium, and Pytest with Page Object Model structure, reusable utilities, and optional submission validation."

