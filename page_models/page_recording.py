from page_models.page_basic_actions import basicActions


class recordingPage(basicActions):
    def __init__(self, page):
        super().__init__(page)

        self.text_to_verify = page.locator("//h1[text()='Audio Recordings']")


    def selectMeetingByName(self, meetingName):
        meeting_xpath = f"//table/tbody/tr/td[text()='{meetingName}']"
        return self.page.locator(meeting_xpath)

    def selectMeetingByNumber(self, num):
        meeting_xpath = f"//table/tbody/tr[{num}]/td[2]"
        return self.page.locator(meeting_xpath)

    def returnPageElement(self, name):
        name = name.lower()
        switcher = {
            'anchor': self.text_to_verify,
        }
        return switcher.get(name, "nothing")