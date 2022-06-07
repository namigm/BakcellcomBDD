from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pyautogui


@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('Open the bakcell.com')
def step_impl(context):
    context.driver.get('https://www.bakcell.com')
    context.driver.maximize_window()


@when('Click the search button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[@id='masthead']/nav/div/div/div/i").click()


@when('Input the "{search_param}"')
def step_impl(context, search_param):
    searchFld = context.driver.find_element(By.ID, "q")
    searchFld.send_keys(search_param)
    context.value = search_param
    pyautogui.press('Enter')


@then('Check the search result')
def step_impl(context):
    try:
        context.searchRes = \
            int(context.driver.find_element(By.XPATH, '//*[@id="content"]/article/section/div[2]/div/div/header/small')
                .text[33])
    except FileNotFoundError:
        print('Search result is not found')
        context.driver.close()
    if context.value == 'Tarif':
        if context.searchRes > 0:
            assert True, "Test passed"
        else:
            assert False
    elif context.value == 'ijdijd':
        if context.searchRes == 0:
            assert True
        else:
            assert False
    elif context.value == 'ptsa':
        if context.searchRes == 0:
            assert True
        else:
            assert False


