"""
Setup and teardown to be run before/after each stage of the test run.
"""
from selenium import webdriver


DEBUG_ON_ERROR = False


def setup_debug_on_error(userdata):
    global DEBUG_ON_ERROR
    DEBUG_ON_ERROR = userdata.getbool("DEBUG_ON_ERROR")


def before_all(context):
    setup_debug_on_error(context.config.userdata)


def before_feature(context, feature):
    pass


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()


def before_step(context, step):
    pass


def after_step(context, step):
    """
    Zoom in on failure location using ipdb
    """
    if DEBUG_ON_ERROR and step.status == "failed":
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_scenario(context, scenario):
    context.browser.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    pass
