from page_models.page_basic_actions import basicActions


class transcriptPage(basicActions):
    def __init__(self, page):
        super().__init__(page)

        self.meeting_type = page.locator("//div[text()='Select Meeting Type']/parent::div/following-sibling::div/i")
        self.tags_type = page.locator("//div[text()='Tags']/parent::div/following-sibling::div/i")

    def verifyByTranscriptName(self, name):
        transcript_locator = self.page.locator("//h6[text()='{name}']")
        #transcript_locator.wait_for(state='visible')
        super().waitToLoadElement(transcript_locator)


    def returnPageElement(self, name):
        name = name.lower()
        switcher = {
            'meetings': self.meeting_type,
            'tags': self.tags_type,
        }
        return switcher.get(name, "nothing")