import pytest
import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import Severity
from selenium.webdriver import Keys
import platform


class ContactDetails(BasePage):

    _ADDRESS_STREET_1 = "//label[text()='Street 1']/following::input[1]"
    _ADDRESS_STREET_2 = "//label[text()='Street 2']/following::input[1]"
    _ADDRESS_STREET_CITY = "//label[text()='City']/following::input[1]"
    _STATE_PROVINCE = "//label[text()='State/Province']/following::input[1]"
    _ZIP_CODE_POSTAL = "//label[text()='Zip/Postal Code']/following::input[1]"
    _COUNTRY = "//div[@class='oxd-select-text-input']"

    @pytest.mark.smoke
    @allure.step("Заполнение первого адресса (street_1)")
    @allure.severity(Severity.NORMAL)
    def address_street1(self,street_one: str):
        address1 = self.wait.until(EC.element_to_be_clickable(self._ADDRESS_STREET_1))
        current_address = address1.get_attribute("value")
        address1.clear()
        if platform.system() == "Darwin":
            address1.send_keys(Keys.COMMAND + "a")
        else:
            address1.send_keys(Keys.CONTROL + "a")

        address1.send_keys(Keys.BACKSPACE)
        address1.send_keys(Keys.DELETE)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Delete data first name",
            attachment_type=allure.attachment_type.PNG
        )

        address1.send_keys(street_one)
        assert address1.get_attribute("value") != current_address, f"Значение не поменялось {street_one}"

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Delete data first name",
            attachment_type=allure.attachment_type.PNG
        )
