import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def to_url(self, url):
        self._driver.get(url)

    def sleep(self, sec):
        time.sleep(sec)

    def wait(self, fn):
        return WebDriverWait(self._driver, 5).until(fn)

    def wait_until_visible(self, by, value):
        return self.wait(EC.visibility_of_element_located((by, value)))

    def wait_until_drag_and_drop(self, by, value):
        return self.wait(EC.visibility_of_element_located((by, value)))
        # #panel_basic > div:nth-child(5)
