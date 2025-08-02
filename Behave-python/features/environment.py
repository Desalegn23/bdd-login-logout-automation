"""
Environment setup and teardown for Behave tests.
This file handles the test environment configuration.
"""
from behave import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import os

# Use the @fixture decorator to register the hooks
@fixture
def browser_setup(context):
    """Setup and teardown for the browser."""
    before_scenario(context, None)  # Pass None as scenario since we don't need it
    yield
    after_scenario(context, None)  # Pass None as scenario since we don't need it

TIMEOUT = 10

def before_all(context):
    """Run before all scenarios."""
    # Set up any global test environment settings here
    pass

def after_all(context):
    """Run after all scenarios."""
    # Clean up any global test environment settings here
    pass

def before_feature(context, feature):
    """Run before each feature."""
    pass

def after_feature(context, feature):
    """Run after each feature."""
    pass

def before_scenario(context, scenario):
    """Run before each scenario."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    if os.getenv("HEADLESS") == "1":
        chrome_options.add_argument("--headless=new")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(TIMEOUT)
    context.wait = WebDriverWait(context.driver, TIMEOUT)

def after_scenario(context, scenario):
    """Run after each scenario."""
    if hasattr(context, 'driver'):
        context.driver.quit()
