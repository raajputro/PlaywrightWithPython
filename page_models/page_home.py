from page_models.page_basic_actions import basicActions

class homePage(basicActions):
    def __init__(self, page):
        super().__init__(page)

        self.home_page_element = page.locator("//span[text()='HR processes.']")
        self.login_btn_element = page.locator("//button/span/span[text()='Login']")
        self.signup_btn_element = page.locator("//button/span/span[text()='Sign-up']")
        self.page_txt_element = page.locator("//h1[text()='Hi there,']")

    # Actions available in this page
    def clickOnLoginBtn(self):
        self.clickOnBtn(self.login_btn_element)

    def clickOnSignupBtn(self):
        self.clickOnBtn(self.signup_btn_element)