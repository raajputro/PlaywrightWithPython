import sys
import os
from playwright.sync_api import sync_playwright

from page_models.page_login import loginPage

sys.path.append(os.getcwd())
from page_models.page_home import homePage

# Test
with sync_playwright() as playwright:
    # Launch the browser
    browser = playwright.chromium.launch()  # or 'firefox'/'webkit'
    page = browser.new_page()
    home_page = homePage(page)
    home_page.navigate("https://dev-meetingspace.askmak.ai")
    home_page.verifyPageLoad()
    page.screenshot(path=os.getcwd()+"/screenshot1.png")

    login_page = loginPage(page)
    login_page.user_login(username="najib@inument.com", password="mE@020486")