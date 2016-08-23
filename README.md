# todomvc_test
Selenium webdriver , python , behave

## Requirements/Installation
#### MacOS (OS X)
    brew install chromedriver
    brew services start chromedriver

#### Pip
Assuming virtualenvwrapper is installed
    
    $ mkvirtualenv todomvc_tests
    @ git clone git@git:williamdanger/todomvc_test
    $ cd todomv_test
    
## Usage  
##### Basic `behave` usage    
    $ cd todomvc_test
    $ behave
    
#####Increase verbosity
    $ beahve -v
    
#####Filter test runs by tag, for example priority

    $ behave --tags p0
    
    
 ## Adding Tests
 
 #### Gherkin
 Gherkin is a DSL for describing test behaviors with a `Given`, `When`, `Then` syntax
 
 #### Step Implementations
 Each line of Gherkin is parsed and matched to a python function by the behave runner.
 
 ##### Context object
 Context is cleared between scenarios. `browser` instance per scenario.
 
 
 ## Debugging Test Failures
`ipdb` can be invoked on test failure by setting the `DEBUG_ON_ERROR` flag.

    $ behave -v -D DEBUG_ON_ERROR

This debugging flag has two advantages.
1. Verify the test code with `ipdb`
2. Keep the WebDriver browser open to inspect