import os
import time
import logging
from behave import given, when, then, step_matcher
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
BASE_URL = "https://www.saucedemo.com/"
TIMEOUT = 10

# Page Element Locators
class LoginPageLocators:
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message-container")

class DashboardPageLocators:
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    APP_LOGO = (By.CLASS_NAME, "app_logo")

def before_scenario(context, scenario):
    """Setup before each scenario."""
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        
        # For headless mode (uncomment if needed)
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        
        # Explicitly set the ChromeDriver version and platform
        chrome_version = "114.0.5735.90"  # Stable version known to work well
        driver_path = ChromeDriverManager(version=chrome_version).install()
        
        # Initialize the Chrome WebDriver with the specified options
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Set up waits
        context.driver.implicitly_wait(TIMEOUT)
        context.wait = WebDriverWait(context.driver, TIMEOUT)
        logger.info(f"Chrome browser started with ChromeDriver version {chrome_version}")
    except Exception as e:
        logger.error(f"Error initializing WebDriver: {str(e)}")
        raise

def after_scenario(context, scenario):
    """Teardown after each scenario."""
    if hasattr(context, 'driver') and context.driver:
        if scenario.status == 'failed':
            # Take screenshot on failure
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{scenario.name}_{timestamp}.png")
            try:
                context.driver.save_screenshot(screenshot_path)
                logger.info(f"Screenshot saved to {screenshot_path}")
            except Exception as e:
                logger.error(f"Failed to take screenshot: {str(e)}")
        
        # Close the browser
        context.driver.quit()
        logger.info("Browser closed")

# Common step definitions
@given('I am on the login page')
def step_on_login_page(context):
    """Navigate to the login page."""
    try:
        context.driver.get(BASE_URL)
        context.wait.until(EC.presence_of_element_located(LoginPageLocators.USERNAME_FIELD))
        logger.info("Navigated to login page")
    except Exception as e:
        logger.error(f"Failed to navigate to login page: {str(e)}")
        raise

@when('I login with username "{username}" and password "{password}"')
def step_login(context, username, password):
    """Perform login with given credentials."""
    try:
        # Clear and enter username
        username_field = context.wait.until(EC.visibility_of_element_located(LoginPageLocators.USERNAME_FIELD))
        username_field.clear()
        username_field.send_keys(username)
        
        # Clear and enter password
        password_field = context.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
        
        # Click login button
        login_button = context.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_button.click()
        logger.info(f"Attempted login with username: {username}")
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        raise

@then('I should see the dashboard')
def step_dashboard(context):
    """Verify that the dashboard is displayed."""
    try:
        context.wait.until(EC.presence_of_element_located(DashboardPageLocators.APP_LOGO))
        assert "inventory" in context.driver.current_url, "Not on dashboard page"
        logger.info("Successfully logged in and dashboard is displayed")
    except Exception as e:
        logger.error(f"Dashboard verification failed: {str(e)}")
        raise

@given('I am logged in as "{username}" with password "{password}"')
def step_logged_in(context, username, password):
    """Log in with the given credentials."""
    step_on_login_page(context)
    step_login(context, username, password)
    step_dashboard(context)

@when('I logout')
def step_logout(context):
    """Perform logout action."""
    try:
        # Click menu button
        menu_button = context.wait.until(EC.element_to_be_clickable(DashboardPageLocators.MENU_BUTTON))
        menu_button.click()
        
        # Click logout link
        logout_link = context.wait.until(EC.element_to_be_clickable(DashboardPageLocators.LOGOUT_LINK))
        logout_link.click()
        logger.info("Logged out successfully")
    except Exception as e:
        logger.error(f"Logout failed: {str(e)}")
        raise

@then('I should be redirected to the login page')
def step_redirected_login(context):
    """Verify redirection to login page after logout."""
    try:
        context.wait.until(EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        assert "saucedemo.com" in context.driver.current_url, "Not on login page"
        logger.info("Successfully redirected to login page")
    except Exception as e:
        logger.error(f"Login page redirection verification failed: {str(e)}")
        raise

@then('I should see an error message "{error_message}"')
def step_error_message(context, error_message):
    """Verify error message is displayed."""
    try:
        error_elem = context.wait.until(
            EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE)
        )
        assert error_message in error_elem.text, f"Expected error message not found. Actual: {error_elem.text}"
        logger.info(f"Verified error message: {error_message}")
    except Exception as e:
        logger.error(f"Error message verification failed: {str(e)}")
        raise

@then('I should not see the dashboard')
def step_not_dashboard(context):
    """Verify that the dashboard is not displayed."""
    try:
        assert "inventory" not in context.driver.current_url, "Unexpectedly on dashboard page"
        logger.info("Successfully verified not on dashboard")
    except Exception as e:
        logger.error(f"Dashboard presence verification failed: {str(e)}")
        raise
