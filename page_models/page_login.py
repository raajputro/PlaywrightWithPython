from playwright.sync_api import expect
import os

class loginPage:
    def __init__(self, page):
        self.page = page
        self.user_name_elem = page.locator("//input[@id='username']")
        self.user_pass_elem = page.locator("//input[@id='password']")
        self.user_login_elem = page.locator("//button[text()='Continue']")



    def verify_page_title(self, title):
        expect(self.page).to_have_title(title)


    def user_login(self, username, password):
        self.verify_page_title("Log in | Meeting Space")
        self.page.screenshot(path=os.getcwd()+"/ss_login_page.png")
        self.user_name_elem.fill(username)
        self.user_pass_elem.fill(password)
        self.user_login_elem.click()
        self.verify_page_title("humaneer")
        self.page.screenshot(path=os.getcwd()+"/ss_home_page.png")

