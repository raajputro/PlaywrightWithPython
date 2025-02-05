import os
from time import time
import sys
sys.path.append(os.getcwd())
from page_models.page_login import loginPage
from page_models.page_home import homePage
from page_models.page_dashboard import dashboardPage

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def resource():
    with sync_playwright() as playwright:
        # Launch the browser
        browser = playwright.chromium.launch()  # or 'firefox'/'webkit'
        page = browser.new_page()
        yield page
        browser.close()

def getScreenShot(pageObj, name):
    pageObj.screenshot(path=os.getcwd() + "/screenshots/" + name + ".png")

def performHomePage(h_page):
    h_page.navigateToUrl("https://dev-meetingspace.askmak.ai")
    h_page.verifyByTitle("humaneer")
    h_page.getScreenshot("1_ss_landing_page" + str(time()))
    h_page.clickOnLoginBtn()

def performLoginPage(l_page):
    l_page.verifyByTitle("Log in | Meeting Space")
    l_page.getScreenshot("2_ss_login_page" + str(time()))
    l_page.user_login(username="najib@inument.com", password="mE@020486")

def performDashboardPage(d_page):
    d_page.verifyByElement()
    d_page.getScreenshot("3_ss_dashboard_page" + str(time()))


# Tests are written
def test_home_page(resource):
    home_page = homePage(resource)
    performHomePage(home_page)

def test_login_page(resource):
    home_page = homePage(resource)
    performHomePage(home_page)
    login_page = loginPage(resource)
    performLoginPage(login_page)

def test_dashboard_page(resource):
    home_page = homePage(resource)
    performHomePage(home_page)
    login_page = loginPage(resource)
    performLoginPage(login_page)
    dashboard_page = dashboardPage(resource)
    performDashboardPage(dashboard_page)