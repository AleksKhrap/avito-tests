from selenium.common.exceptions import NoSuchElementException
import os


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_an_element(self, how, what):
        try:
            element = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return element

    def take_a_screenshot(self, how, what, name):
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        element = self.find_an_element(how, what)
        screenshot_path = os.path.join(output_dir, f"{name}.png")
        element.screenshot(screenshot_path)
