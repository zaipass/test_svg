from testcase.test_flow import TestFlow
from testcase.test_login import TestLogin


def test_flow(web_driver):
     test_login_actions = TestLogin(web_driver)
     test_login_actions.wait_for_login()

     test_flow_actions = TestFlow(web_driver)
     test_flow_actions.test_drag_drop()