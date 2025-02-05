from playwright.sync_api import expect
from page_models.page_basic_actions import basicActions


class dashboardPage(basicActions):
    def __init__(self, page):
        super().__init__(page)

        self.page_txt_element = page.locator("//h1[text()='Hi there,']")

    def verifyByElement(self):
        expect(self.page_txt_element).to_be_visible()