from behave import given, then, when
from hamcrest import assert_that, has_string
from selenium.webdriver.support.ui import WebDriverWait

@given('TodoMVC is opened in the browser')
@when('TodoMVC is opened in the browser')
def step_navigate_to_todomvc(context):
    """
    Navigate to TodoMVC example site

    :type context: behave.runner.Context
    """
    context.browser.get("http://todomvc.com/examples/react/#/")


@then('the title reads "{desired_title}"')
def step_verify_page_title(context, desired_title):
    """
    Verify page title matches given string

    :param desired_title: Desired page title
    :type context: behave.runner.Context
    """
    title = context.browser.title.encode('utf-8')
    page_title = desired_title.encode('utf-8')
    assert_that(title, has_string(page_title))
