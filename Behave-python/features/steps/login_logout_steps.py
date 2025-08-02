from behave import given, when, then, fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@fixture
def browser_chrome(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)
    yield context.driver
    context.driver.quit()

def before_all(context):
    use_fixture(browser_chrome, context)

def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()

@given('I am on the login page')
def step_impl(context):
    context.driver.get(LOGIN_URL)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )

@when('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

@then('I should see the dashboard')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    assert "inventory" in context.driver.current_url

@given('I am logged in as "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.driver.get(LOGIN_URL)
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    context.driver.find_element(By.ID, "user-name").send_keys(username)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))
    )

@when('I logout')
def step_impl(context):
    menu_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_btn.click()
    logout_btn = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_btn.click()

@then('I should be redirected to the login page')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-button"))
    )
    assert "saucedemo.com" in context.driver.current_url
