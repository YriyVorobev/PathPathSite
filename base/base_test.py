import allure
from data.credentials import Credentials
from pages.login_page.page import LoginPage
from pages.dashboard_page.page import Dashboard
from pages.my_info_page.page import MyInfoPage

class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.dashboard = Dashboard(self.driver)
        self.my_info_page = MyInfoPage(self.driver)