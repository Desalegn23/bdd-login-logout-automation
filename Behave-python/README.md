# Behave BDD Suite: Login & Logout on saucedemo.com

## Overview 🚀
This project is a minimal Python BDD automation suite using Behave to test the login and logout flows on [saucedemo.com](https://www.saucedemo.com). It demonstrates best practices for Gherkin scenarios, Selenium automation, and BDD structure.

## Quick Start 📦

**1. Create & activate a virtual environment**

*Unix/macOS:*
```sh
python3 -m venv .venv
source .venv/bin/activate
```

*Windows:*
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**2. Install dependencies**
```sh
pip install -r requirements.txt
```

**3. Run tests**
```sh
behave
```

**4. Filter scenarios by tags**
```sh
behave -t @login
behave -t @logout
```

**5. Headless run (set environment variable)**
```sh
HEADLESS=1 behave
```

## Covered Scenarios 🧪
| Tag     | Scenario Description                                 |
|---------|-----------------------------------------------------|
| @login  | Successful login with valid credentials              |
| @logout | Logout from dashboard, verify return to login page   |

## Tech Stack ⚙️
- Python 3.x
- Behave
- Selenium WebDriver (Chrome)
- behave-html-formatter

## Browser Setup
- Chrome browser must be installed.
- ChromeDriver is auto-managed by Selenium (if not, download from [ChromeDriver site](https://chromedriver.chromium.org/downloads)).
- Headless mode is enabled by default for CI and quick runs.

## Adding New Scenarios
1. Add new Gherkin scenarios to `features/login_logout.feature`.
2. Implement step definitions in `features/steps/login_logout_steps.py`.
3. Use tags (e.g., `@login`, `@logout`) for easy filtering.

## Contributing
Pull requests and suggestions are welcome! Please follow PEP8 and Behave best practices.

## License
MIT License
