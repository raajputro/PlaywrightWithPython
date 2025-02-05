# import base64
# import re
# from playwright.sync_api import Page, expect
#
# def test_has_title(page: Page):
#     page.goto("https://playwright.dev/")
#
#     expect(page).to_have_title(re.compile("Playwright"))
#
# def test_get_started_link(page: Page):
#     page.goto("https://playwright.dev/")
#
#     page.get_by_role("link", name="Get started").click()
#
#     expect(page.get_by_role("heading", name="Installation")).to_be_visible()
#     page.screenshot(path="../screenshot.png")
#     # screenshot_bytes = page.screenshot()
#     # print(base64.b64encode(screenshot_bytes).decode())


import itertools
import numpy as np
data = [1,2]
result = list(itertools.permutations(data))
for r in result:
    print(r)
print("Print using numpy")
print(np.matrix(result))