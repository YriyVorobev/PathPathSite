import allure
import logging

import pytest

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import Severity
from selenium.webdriver import Keys

class PersonalDetailsComponents(BasePage):

    _FIRST_NAME = "//input[@name='firstName']"
    _MIDDLE_NAME = "//input[@name='middleName']"
    _LAST_NAME = "//input[@name='lastName']"
    _EMPLOYEE_ID = "//label[text()='Employee Id']/following::input[1]"
    _OTHER_ID = "//label[text()='Other Id']/following::input[1]"
    _SAVE_ONE_SUBMIT_BUTTON = "(//button[@type='submit'])[1]"

    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    @allure.step("Name changes")
    def change_first_name(self,first_name):
        frist_name_field = self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME))
        current_value = frist_name_field.get_attribute("value")
        frist_name_field.send_keys(Keys.COMMAND + "A")
        frist_name_field.send_keys(Keys.BACKSPACE)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Delete data first name",
            attachment_type=allure.attachment_type.PNG
        )
        frist_name_field.send_keys(first_name)
        assert frist_name_field.get_attribute("value") == first_name, f"Значения {first_name}не поменялось"
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Имя поменяли",
            attachment_type=allure.attachment_type.PNG
        )

    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    @allure.step("Changes middle name")
    def changed_middle_name(self, middle_name):
        middle_name_field = self.wait.until(EC.element_to_be_clickable(self._MIDDLE_NAME))
        middle_name_field.send_keys(Keys.COMMAND + "A")
        middle_name_field.send_keys(Keys.BACKSPACE)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Проверяем пусто ли поле middle_name",
            attachment_type=allure.attachment_type.PNG
        )
        middle_name_field.send_keys(middle_name)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Проверяем поле middle_name",
            attachment_type=allure.attachment_type.PNG
        )
        assert middle_name_field.get_attribute("value") == middle_name, f"Значения {middle_name}не поменялось"

    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    @allure.step("Changes Last Name")
    def last_name_changed(self,last_name):
        last_name_field = self.wait.until(EC.element_to_be_clickable(self._LAST_NAME))
        last_name_field.send_keys(Keys.COMMAND + "A")
        last_name_field.send_keys(Keys.BACKSPACE)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name= "changed last name",
            attachment_type=allure.attachment_type.PNG
        )
        last_name_field.send_keys(last_name)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name= "changed last name",
            attachment_type=allure.attachment_type.PNG
        )
        assert last_name_field.get_attribute("value") == last_name, f"Значения {last_name} не поменялось"


    @pytest.mark.smoke
    @allure.severity(Severity.BLOCKER)
    @allure.step("Changes Employee ID ")
    def changed_employee_id(self,employee_id):
        employee_id_field = self.wait.until(EC.element_to_be_clickable(self._EMPLOYEE_ID))
        employee_id_field.send_keys(Keys.COMMAND + "A")
        employee_id_field.send_keys(Keys.BACKSPACE)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Меняем Employee ID",
            attachment_type=allure.attachment_type.PNG

        )
        employee_id_field.send_keys(employee_id)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Меняем Employee ID",
            attachment_type=allure.attachment_type.PNG

        )
        assert employee_id_field.get_attribute("value") == employee_id, f"Значения {employee_id}не поменялось"


    @pytest.mark.smoke
    @allure.step("Changes Other id")
    @allure.severity(Severity.BLOCKER)
    def changed_other_id(self,other_id):
        other_id_field = self.wait.until(EC.element_to_be_clickable(self._OTHER_ID))
        other_id_field.send_keys(Keys.COMMAND + "A")
        other_id_field.send_keys(Keys.BACKSPACE)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Changed Other ID Clear",
            attachment_type=allure.attachment_type.PNG
        )
        other_id_field.send_keys(other_id)
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Changed Other ID fill in",
            attachment_type=allure.attachment_type.PNG
        )
        assert other_id_field.get_attribute("value") == other_id, f"Значения {other_id}не поменялось"



    @allure.step("Нажатия по кнопке")
    def save_changed(self):
        self.wait.until(EC.element_to_be_clickable(self._SAVE_ONE_SUBMIT_BUTTON)).click()




