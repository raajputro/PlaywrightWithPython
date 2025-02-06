from playwright.sync_api import expect
from page_models.page_basic_actions import basicActions


class dashboardPage(basicActions):
    def __init__(self, page):
        super().__init__(page)

        self.page_txt_element = page.locator("//h1[text()='Hi there,']")

        self.action_card_ask_elem = page.locator("//div[@class='action-card']/child::div/h4[text()='Ask']")
        self.action_card_action_elem = page.locator("//div[@class='action-card']/child::div/h4[text()='Action']")
        self.action_card_meet_elem = page.locator("//div[@class='action-card']/child::div/h4[text()='Meet']")

        self.meeting_item_1 = page.locator("//ul[@class='meeting-items']/li[1]/div/p/a")
        self.meeting_item_2 = page.locator("//ul[@class='meeting-items']/li[2]/div/p/a")
        self.meeting_item_3 = page.locator("//ul[@class='meeting-items']/li[3]/div/p/a")

        self.side_bar_1_item_1 = page.locator("//div[@class='q-list'][1]/div/div[contains(text(),'Home')]")
        self.side_bar_1_item_2 = page.locator("//div[@class='q-list'][1]/div/div[contains(text(),'Recordings')]")
        self.side_bar_1_item_3 = page.locator("//div[@class='q-list'][1]/div/div[contains(text(),'Meetings')]")
        self.side_bar_1_item_4 = page.locator("//div[@class='q-list'][1]/div/div[contains(text(),'Documents')]")
        self.side_bar_1_item_5 = page.locator("//div[@class='q-list'][1]/div/div[contains(text(),'Quick Record')]")
        self.side_bar_1_item_6 = page.locator("//div[@class='q-list'][1]/div/div[contains(text(),'HeyMak')]")

        self.side_bar_2_item_1 = page.locator("//div[@class='q-list'][2]/div/div/div[contains(text(),'Community')]")
        self.side_bar_2_item_2 = page.locator("//div[@class='q-list'][2]/div/div/div[contains(text(),'Help')]")
        self.side_bar_2_item_3 = page.locator("//div[@class='q-list'][2]/div/div/div[contains(text(),'Logout')]")


    def verifyByElement(self):
        expect(self.page_txt_element).to_be_visible()


    def returnPageElement(self, name):
        name = name.lower()
        switcher = {
            'home': self.side_bar_1_item_1,
            'recording': self.side_bar_1_item_2,
            'meetings': self.side_bar_1_item_3,
            'documents': self.side_bar_1_item_4,
            'quick record': self.side_bar_1_item_5,
            'mak': self.side_bar_1_item_6,
            'community': self.side_bar_2_item_1,
            'help': self.side_bar_2_item_2,
            'logout': self.side_bar_2_item_3,
            'ask': self.action_card_ask_elem,
            'action': self.action_card_action_elem,
            'meet': self.action_card_meet_elem,
            'meeting1': self.meeting_item_1,
            'meeting2': self.meeting_item_2,
            'meeting3': self.meeting_item_3,
        }
        return switcher.get(name,'nothing')
