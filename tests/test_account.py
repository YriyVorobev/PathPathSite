import time
from time import sleep

import allure
from base.base_test import BaseTest

@allure.epic("Test Changed")
@allure.feature("Login in")
class TestAccount(BaseTest):


    @allure.story("Test Login in")
    def test_change_name(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
    @allure.story("Test opened page")
    def test_dashboard_opened(self):
        self.dashboard.is_opened()
        self.dashboard.go_to_my_info_page()
        self.my_info_page.is_opened()

    @allure.story("test fill out my info page")
    def test_my_info_fill_out(self):
        self.my_info_page.personal_details.change_first_name("Доулинго")
        self.my_info_page.personal_details.changed_middle_name("Доулингович")
        self.my_info_page.personal_details.last_name_changed("Даркнетович")
        self.my_info_page.personal_details.changed_employee_id("12345")
        self.my_info_page.personal_details.changed_other_id("12345")
        self.my_info_page.personal_details.drivers_licence_numbers("12330")
        self.my_info_page.personal_details.licence_expire_date("2025-18-12")
        self.my_info_page.personal_details.date_of_birth("1997-14-10")
        self.my_info_page.personal_details.gender_male()
        self.my_info_page.personal_details.save_changed()
        self.my_info_page.personal_details.test_field("323435")
        self.my_info_page.personal_details.browser_load()
        self.my_info_page.personal_details.click_button_save()




