from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given(u'Launch chrome driver')
def launch_ghm(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when(u'Open the main page og bakcell.com')
def open_bakcellcom(context):
    context.driver.get('https://www.bakcell.com')


@then(u'Verify the homepage title')
def homepage_title(context):
    actual_driver = context.driver.title
    if actual_driver == 'Bakcell':
        assert True
    else:
        assert False


@then(u'Close the browser')
def close_browser(context):
    context.driver.close()
