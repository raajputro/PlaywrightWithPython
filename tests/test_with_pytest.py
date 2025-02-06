import os
from time import time
import sys
sys.path.append(os.getcwd())
from page_models.page_login import loginPage
from page_models.page_home import homePage
from page_models.page_dashboard import dashboardPage

import pytest
from playwright.sync_api import sync_playwright

current_directory = os.getcwd()
print(current_directory)

@pytest.fixture(scope='session', autouse=True)
def resource():
    with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch()  # or 'firefox'/'webkit'
        page = browser.new_page()
        yield page
        browser.close()

def getScreenShot(pageObj, name):
    pageObj.screenshot(path=current_directory + "/screenshots/" + name + ".png")
    #pageObj.screenshot(path=current_directory + "/screenshots/" + name + "-" + str(time()) + ".png")

# Tests are written
def test_home_page(resource):
    h_page = homePage(resource)
    h_page.navigateToUrl("https://dev-meetingspace.askmak.ai")
    h_page.verifyByTitle("humaneer")
    getScreenShot(resource, name="ss_landing_page")
    elem = h_page.returnPageElement('login')
    h_page.clickOnBtn(elem)

def test_login_page(resource):
    #test_home_page(resource)
    l_page = loginPage(resource)
    l_page.verifyByTitle("Log in | Meeting Space")
    getScreenShot(resource, name="ss_login_page")
    l_page.user_login(username="najib@inument.com", password="mE@020486")

def test_dashboard_page(resource):
    #test_login_page(resource)
    d_page = dashboardPage(resource)
    #d_page.verifyByElement()
    elem = d_page.returnPageElement('home')
    d_page.waitToLoadElement(elem)
    getScreenShot(resource, name="ss_dashboard_page")

def test_go_to_recording_from_dashboard(resource):
    d_page = dashboardPage(resource)
    elem = d_page.returnPageElement('recording')
    d_page.clickOnElement(elem)
    elem = d_page.returnPageElement('home')
    d_page.waitToLoadElement(elem)
    getScreenShot(resource, name="ss_recording_page")
    d_page.clickOnElement(elem)
