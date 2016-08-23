from behave import given, then, when
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@given('a todo for "{todo}" is added')
@when('a todo for "{todo}" is added')
def step_add_todo(context, todo):
    """
    Add a todo to the todo list

    :param todo: Text of Todo entry to be added
    :type context: behave.runner.Context
    """
    todo_textbox = context.browser.find_element_by_class_name("new-todo")
    todo_textbox.send_keys(todo)
    todo_textbox.send_keys(Keys.RETURN)


@when('the todo "{complete_todo}" is marked complete')
def step_mark_todo_complete(context, complete_todo):
    """
    Mark todo as completed

    :type context: behave.runner.Context
    """
    context.browser.find_element_by_class_name("toggle").click()


@when('the todo "{deleted_todo}" is deleted')
def step_delete_todo(context, deleted_todo):
    """
    :param deleted_todo: Todo entry to delete
    :type context: behave.runner.Context
    """
    todo_line = context.browser.find_element_by_class_name("view")
    delete_button = context.browser.find_element_by_class_name("destroy")
    ActionChains(context.browser).move_to_element(todo_line).click(delete_button).perform()


@when('the todo "{target_todo}" is modified to "{new_todo}"')
def step_modify_todo(context, target_todo, new_todo):
    """
    :type context: behave.runner.Context
    """
    # Double click existing todo
    todo_reactid = context.browser.find_element_by_xpath(
        "//input[@value='{}']".format(target_todo)).get_attribute("data-reactid")

    reactid = todo_reactid[:-2]

    todo_line = context.browser.find_element_by_xpath(
        "//li[@data-reactid='{}']".format(reactid))

    ActionChains(context.browser).double_click(todo_line).send_keys(Keys.CLEAR).send_keys(new_todo).perform()


@then('the todo list contains "{desired_todo}"')
def step_verify_todo(context, desired_todo):
    """
    Find element matching desired_todo

    :param desired_todo: Todo entry to verify
    :type context: behave.runner.Context
    """
    assert context.browser.find_element_by_xpath("//input[@value='{}']".format(desired_todo))


@then('todo "{completed_todo}" is checked off')
def step_verify_completed_task(context, completed_todo):
    """
    :type context: behave.runner.Context
    """
    todo_reactid = context.browser.find_element_by_xpath(
        "//label['{}']".format(completed_todo)).get_attribute('data-reactid')

    reactid_base = todo_reactid.split(".")[:-2]
    reactid = '.'.join(reactid_base)

    assert context.browser.find_element_by_xpath(
        "//li[@data-reactid='{}']".format(reactid)
    )


@then('the todo list does not contain "{deleted_todo}"')
def step_todo_not_in_list(context, deleted_todo):
    """
    Try to find the deleted todo, pass if not found
    :type context: behave.runner.Context
    """
    try:
        missing_todo = context.browser.find_element_by_xpath(
            "//input[@value='{}']".format(deleted_todo))
    except NoSuchElementException:
        pass
