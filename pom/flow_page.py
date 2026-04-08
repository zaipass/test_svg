from selenium.webdriver import ActionChains

from common.base_page import BasePage

URL = 'https://www.processon.com/diagraming/69d3695cf702dc610b883ed7?from=pwa'


class FlowPage(BasePage):
    def goto_flow_page(self):
        self.to_url(URL)

    def drag_and_drop(self, by, value):
        dom = self.wait_until_drag_and_drop(by, value)
        actions = ActionChains(self._driver)
        actions.move_to_element(dom)
        actions.double_click(dom)
        actions.perform()
        self.sleep(20)
