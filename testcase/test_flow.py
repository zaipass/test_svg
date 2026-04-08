from selenium.webdriver.common.by import By

from common.base_page import BasePage
from pom.flow_page import FlowPage


class TestFlow(BasePage):
    def test_drag_drop(self):
        page = FlowPage(self._driver)
        page.goto_flow_page()
        page.drag_and_drop(By.CSS_SELECTOR, "#panel_basic > div:nth-child(5)")
