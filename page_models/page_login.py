from page_models.page_basic_actions import basicActions


class loginPage(basicActions):
    def __init__(self, page):
        super().__init__(page)

        self.user_name_elem = page.locator("//input[@id='username']")
        self.user_pass_elem = page.locator("//input[@id='password']")
        self.user_login_elem = page.locator("//button[text()='Continue']")

    # Actions available in this page
    def user_login(self, username, password):
        self.inputInElement(self.user_name_elem, username)
        self.inputInElement(self.user_pass_elem, password)
        self.clickOnBtn(self.user_login_elem)



