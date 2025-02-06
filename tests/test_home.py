# import sys
# import os
#
# from playwright.sync_api import sync_playwright
#
# sys.path.append(os.getcwd())
# from page_models.page_login import loginPage
# from page_models.page_home import homePage
# from page_models.page_dashboard import dashboardPage
#
# # Test
# def getScreenShot(pageObj, name):
#     page.screenshot(path=os.getcwd() + "/screenshots/" + name + ".png")
#
# def performHomePage(h_page):
#     h_page.navigateToUrl("https://dev-meetingspace.askmak.ai")
#     h_page.verifyByTitle("humaneer")
#     getScreenShot(h_page,"1_ss_landing_page")
#     h_page.clickOnLoginBtn()
#
# def performLoginPage(l_page):
#     l_page.verifyByTitle("Log in | Meeting Space")
#     getScreenShot(l_page, "2_ss_login_page")
#     l_page.user_login(username="najib@inument.com", password="mE@020486")
#
# def performDashboardPage(d_page):
#     d_page.verifyByElement()
#     getScreenShot(d_page, "3_ss_dashboard_page")
#
# with sync_playwright() as playwright:
#     # Launch the browser
#     browser = playwright.chromium.launch()  # or 'firefox'/'webkit'
#     page = browser.new_page()
#
#     home_page = homePage(page)
#     performHomePage(home_page)
#
#     login_page = loginPage(page)
#     performLoginPage(login_page)
#
#     dashboard_page = dashboardPage(page)
#     performDashboardPage(dashboard_page)
