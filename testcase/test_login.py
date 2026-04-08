import pickle
from common.base_page import BasePage


URL = 'https://www.processon.com/login?redirect=https://www.processon.com/diagraming/69d3695cf702dc610b883ed7?from=pwa'


class TestLogin(BasePage):
    def wait_for_login(self):
        self._driver.get(URL)

        print("请手动登录...")
        input("登录完成后按回车继续")

        with open('auth_cookies.pkl', 'wb') as f:
            pickle.dump(self._driver.get_cookies(), f)

        self._driver.refresh()

