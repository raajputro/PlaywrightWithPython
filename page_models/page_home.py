from playwright.sync_api import expect


class homePage:
    def __init__(self, page):
        self.page = page
        self.home_page_element = page.locator("//span[text()='HR processes.']")
        self.login_btn_element = page.locator("//button/span/span[text()='Login']")
        self.signup_btn_element = page.locator("//button/span/span[text()='Sign-up']")

    def navigate(self, givenUrl):
        self.page.goto(givenUrl)

    def verifyPageLoad(self):
        expect(self.home_page_element).to_be_visible()