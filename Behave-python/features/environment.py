"""
Environment setup and teardown for Behave tests.
This file handles the test environment configuration.
"""
from behave import fixture
from features.steps.login_logout_steps import before_scenario, after_scenario

# Use the @fixture decorator to register the hooks
@fixture
def browser_setup(context):
    """Setup and teardown for the browser."""
    before_scenario(context, None)  # Pass None as scenario since we don't need it
    yield
    after_scenario(context, None)  # Pass None as scenario since we don't need it

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
    before_scenario(context, scenario)

def after_scenario(context, scenario):
    """Run after each scenario."""
    after_scenario(context, scenario)
