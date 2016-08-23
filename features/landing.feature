Feature: Landing page of TodoMVC app
  Verify page loading and landing

  @p0
  Scenario: Verify page loading and title
    When TodoMVC is opened in the browser
    Then the title reads "React • TodoMVC"