import os
from time import time
import sys

sys.path.append(os.getcwd())
from page_models.page_login import loginPage
from page_models.page_home import homePage
from page_models.page_dashboard import dashboardPage
from page_models.page_recording import recordingPage
from page_models.page_transcript import transcriptPage

import pytest
from playwright.sync_api import sync_playwright

current_directory = os.getcwd()
print(current_directory)
meeting_name = 'D.Beck'

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
    getScreenShot(resource, name="1")
    elem = h_page.returnPageElement('login')
    h_page.clickOnBtn(elem)

def test_login_page(resource):
    l_page = loginPage(resource)
    l_page.verifyByTitle("Log in | Meeting Space")
    getScreenShot(resource, name="2")
    l_page.user_login(username="najib@inument.com", password="mE@020486")

def test_dashboard_page(resource):
    d_page = dashboardPage(resource)
    elem = d_page.returnPageElement('home')
    d_page.waitToLoadElement(elem)
    getScreenShot(resource, name="3")

def test_go_to_recording_from_dashboard(resource):
    d_page = dashboardPage(resource)
    elem = d_page.returnPageElement('recording')
    d_page.clickOnElement(elem)
    elem = d_page.returnPageElement('home')
    d_page.waitToLoadElement(elem)
    getScreenShot(resource, name="4")
    #d_page.clickOnElement(elem)

def test_goto_meeting(resource):
    r_page = recordingPage(resource)
    elem = r_page.returnPageElement('anchor')
    r_page.waitToLoadElement(elem)
    getScreenShot(resource, "5")
    elem = r_page.selectMeetingByName(meeting_name)
    r_page.waitToLoadElement(elem)
    getScreenShot(resource, "6")
    r_page.clickOnElement(elem)
    getScreenShot(resource, "7")

def check_transcript_details(resource):
    t_page = transcriptPage(resource)
    t_page.verifyByTranscriptName(meeting_name)
    getScreenShot(resource,"8")
    elm = t_page.returnPageElement('meetings')
    t_page.selectFromListByValue('General Meeting')