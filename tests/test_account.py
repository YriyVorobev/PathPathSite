import time
import allure
from base.base_test import BaseTest
from time import sleep

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
    def test_my_info_fill_out(self,faker_ru):
        self.my_info_page.personal_details.change_first_name(faker_ru.first_name())
        self.my_info_page.personal_details.changed_middle_name(faker_ru.middle_name())
        self.my_info_page.personal_details.last_name_changed(faker_ru.last_name())
        self.my_info_page.personal_details.changed_employee_id(faker_ru.iana_id())
        self.my_info_page.personal_details.changed_other_id(faker_ru.iana_id())
        self.my_info_page.personal_details.drivers_licence_numbers(faker_ru.iana_id())
        self.my_info_page.personal_details.licence_expire_date("2023-23-10")
        self.my_info_page.personal_details.date_of_birth("2020-12-12")
        self.my_info_page.personal_details.gender_male()
        self.my_info_page.personal_details.save_changed()
        self.my_info_page.personal_details.test_field(faker_ru.postcode())
        self.my_info_page.personal_details.browser_load()
        self.my_info_page.personal_details.click_button_save()

    @allure.story("test contact detail")
    def test_contact_detail(self,faker_ru):
        self.my_info_page.go_to_contact_detail()
        self.my_info_page.contact_details.address_street1(faker_ru.street_name())




