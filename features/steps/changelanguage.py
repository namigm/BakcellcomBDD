from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@given(u'Launch browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    time.sleep(3)


@when(u'Open URL')
def step_impl(context):
    context.driver.get("http://bakcell.com")


@when(u'Click button to change page language to ENG')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[contains(text(),'En')]").click()


@then(u'Page language changed to ENG')
def step_impl(context):
    d = context.driver.find_element(By.XPATH, "/html/body").text
    if 'ABOUT' and 'COMPANY' in d:
        print('true')
    else:
        print('false')


@when(u'Click button to change page language to RUS')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Ru')]").click()


@then(u'Page language changed to RUS')
def step_impl(context):
    d = context.driver.find_element(By.XPATH, "/html/body").text
    if 'Вакансии' and 'Подробнее' in d:
        assert True
    else:
        assert False


@when(u'Click button to change page language to AZE')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[contains(text(),'Az')]").click()


@then(u'Page language changed to AZE')
def step_impl(context):
    d = context.driver.find_element(By.XPATH, "/html/body").text
    if 'ŞİRKƏT' and 'HAQQINDA' in d:
        assert True

    else:
        assert False
    context.driver.close()





