from playwright.sync_api import expect
import os

class basicActions:
    def __init__(self, page):
        self.page = page

    def navigateToUrl(self, givenUrl):
        self.page.goto(givenUrl)

    def getScreenshot(self, name):
        self.page.screenshot(path=os.getcwd() + "/screenshots/" + name + ".png")

    def verifyByTitle(self, title):
        expect(self.page).to_have_title(title)

    def verifyByText(self, elem, text):
        expect(elem).to_have_text(text)

    def waitToLoadElement(self, elem):
        expect(elem).to_be_visible()

    def clickOnBtn(self, btn):
        btn.click()

    def clickOnElement(self, elem):
        elem.click()

    def inputInElement(self, elem, inputText):
        elem.click()
        elem.fill(inputText)