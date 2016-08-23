Feature: Adding and Modifying items in the Todo list
  The Todo list is the core feature of the web app under test. Todos can be
  created, modified (marked done) and deleted.

  Background: Navigate to TodoMVC
    Given TodoMVC is opened in the browser

  @p0
  Scenario: Add todo to blank list
    When a todo for "Buy Milk" is added
    Then the todo list contains "Buy Milk"

  @p0
  Scenario: Mark todo as complete
    Given a todo for "Buy Milk" is added
    When the todo "Buy Milk" is marked complete
    Then todo "Buy Milk" is checked off

  @p0
  Scenario: Delete todo
    Given a todo for "Delete me" is added
    When the todo "Delete me" is deleted
    Then the todo list does not contain "Delete me"

  @p0
  Scenario: Modify todo
    Given a todo for "Change me" is added
    When the todo "Change me" is modified to "I changed!"
    Then the todo list contains "I changed!"

  @wip
  @p0
  Scenario: Clear completed button
    Given a completed todo "Clear with the button"
    When the Clear Complete button is pressed
    Then the todo list is emply

  @wip
  @p1
  Scenario: Add multiple todos
    Given a todo for "First Entry" is added
    When a todo for "2nd Entry" is added
      And a todo for "Entry 3.0" is added
    Then the todo list contains