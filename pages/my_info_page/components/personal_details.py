import allure
import logging
import pytest
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import Severity
from selenium.webdriver import Keys
from data.path import CAT_IMAGE


class PersonalDetailsComponents(BasePage):

    _FIRST_NAME = "//input[@name='firstName']"
    _MIDDLE_NAME = "//input[@name='middleName']"
    _LAST_NAME = "//input[@name='lastName']"
    _EMPLOYEE_ID = "//label[text()='Employee Id']/following::input[1]"
    _OTHER_ID = "//label[text()='Other Id']/following::input[1]"
    _DRIVERS_LICENCE_NUMBER = "//label[contains(text(), \"Driver's License\")]/following::input[1]"
    _LICENCE_EXPIRE_DATE = "//label[text()='License Expiry Date']/following::input[1]"
    _DATE_OF_BIRTH = "//label[text()='Date of Birth']/following::input[1]"
    _GENDER_MALE = "//label[normalize-space()='Male']"
    _SAVE_ONE_SUBMIT_BUTTON = "(//button[@type='submit'])[1]"
    _TEST_FIELD = "//label[text()='Test_Field']/following::input[1]"
    _ATTACHMENTS = "//h6[text()='Attachments']/following::button"
    _BROWSER = "//input[@type='file']"
    _SAVE_TWO_SUBMIT_BUTTON = "(//button[@type='submit'])[2]"


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

    @pytest.mark.smoke
    @allure.step("Заполняем Номер водительского удостоверения в поле")
    @allure.severity(Severity.NORMAL)
    def drivers_licence_numbers(self, numbers):
        drivers_licence = self.wait.until(EC.element_to_be_clickable(self._DRIVERS_LICENCE_NUMBER))
        drivers_licence.send_keys(Keys.COMMAND + "A")
        drivers_licence.send_keys(Keys.BACKSPACE)

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="drivers_licence_numbers clear",
            attachment_type=allure.attachment_type.PNG
        )

        drivers_licence.send_keys(numbers)

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="drivers_licence_numbers",
            attachment_type=allure.attachment_type.PNG
        )

        assert drivers_licence.get_attribute("value") == numbers, f"Значение {numbers} не изменилось"

    @pytest.mark.smoke
    @allure.severity(Severity.NORMAL)
    @allure.step("Заполнение Номера водительского удостоверения")
    def licence_expire_date(self,date_expire):
        date_licence = self.wait.until(EC.element_to_be_clickable(self._LICENCE_EXPIRE_DATE))
        date_licence.send_keys(Keys.COMMAND + "A")
        date_licence.send_keys(Keys.BACKSPACE)

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="licence_expire_date clear",
            attachment_type=allure.attachment_type.PNG
        )

        date_licence.send_keys(date_expire)

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="licence_expire_date",
            attachment_type=allure.attachment_type.PNG
        )

        assert date_licence.get_attribute("value") == date_expire, f"Значение {date_expire} не поменялось"

    @pytest.mark.smoke
    @allure.step(" Заполняем Дату рождения")
    @allure.severity(Severity.NORMAL)
    def date_of_birth(self,date_birth):
        birth_of_date = self.wait.until(EC.element_to_be_clickable(self._DATE_OF_BIRTH))
        birth_of_date.send_keys(Keys.COMMAND + "A")
        birth_of_date.send_keys(Keys.BACKSPACE)

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Очистили дату рождения",
            attachment_type=allure.attachment_type.PNG
        )

        birth_of_date.send_keys(date_birth)

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Заполнили дату рождения",
            attachment_type=allure.attachment_type.PNG
        )

        assert birth_of_date.get_attribute("value") == date_birth, f"Значение {date_birth} не поменялось"

    @pytest.mark.smoke
    @allure.step("Выбор пола, нажатием по радиобатону")
    @allure.severity(Severity.NORMAL)
    def gender_male(self):
        self.wait.until(EC.element_to_be_clickable(self._GENDER_MALE)).click()

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Выберете пол",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Нажатия по кнопке")
    def save_changed(self):
        self.wait.until(EC.element_to_be_clickable(self._SAVE_ONE_SUBMIT_BUTTON)).click()

    @pytest.mark.smoke
    @allure.step("Проверка заполнения и затирания значения в поле test_field")
    @allure.severity(Severity.NORMAL)
    def test_field(self, field_test):
        test = self.wait.until(EC.element_to_be_clickable(self._TEST_FIELD))
        test.send_keys(Keys.COMMAND + "A")
        test.send_keys(Keys.BACKSPACE)

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Стерли значение в поле test_field",
            attachment_type=allure.attachment_type.PNG
        )

        test.send_keys(field_test)

        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name="Заполнили значения в поле test_field",
            attachment_type=allure.attachment_type.PNG
        )

        assert test.get_attribute("value") == field_test, f"Значение {field_test} не заполнено"

    @pytest.mark.regression
    @allure.step("Загружаем файл")
    @allure.severity(Severity.BLOCKER)
    def browser_load(self):
        self.wait.until(EC.element_to_be_clickable(self._ATTACHMENTS)).click()
        load_brw = self.wait.until(EC.presence_of_element_located(self._BROWSER))
        load_brw.send_keys(str(CAT_IMAGE))

        allure.attach.file(
            str(CAT_IMAGE),
            name=f"Загруженный файл: {CAT_IMAGE.name}",
            attachment_type=allure.attachment_type.JPG
        )

        assert CAT_IMAGE.exists(), f"Файл не найден: {CAT_IMAGE}"

    @pytest.mark.smoke
    @allure.step("Нажимаем сохранить")
    @allure.severity(Severity.NORMAL)
    def click_button_save(self):
        self.wait.until(EC.element_to_be_clickable(self._SAVE_TWO_SUBMIT_BUTTON)).click()







