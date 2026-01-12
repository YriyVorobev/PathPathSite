import allure
from base.base_page import BasePage
from data.urls import Urls
from pages.my_info_page.components.personal_details import PersonalDetailsComponents
from pages.my_info_page.components.contact_details import ContactDetails
from selenium.webdriver.support import expected_conditions as EC

class MyInfoPage(BasePage):

    _PAGE_URL = Urls.MY_INFO_PAGE
    _CONTACT_DETAIL_TAB ="//a[text()='Contact Details']"

    def __init__(self,driver):
        super().__init__(driver)
        self.personal_details = PersonalDetailsComponents(driver)
        self.contact_details = ContactDetails(driver)


    def go_to_contact_detail(self):
        with allure.step("Переход на страницу контактов"):
            tab = self.wait.until(EC.visibility_of_element_located(self._CONTACT_DETAIL_TAB))
            self.action.move_to_element(tab).click().perform()
            self.wait.until(EC.url_to_be(Urls.CONTACT_DETAILS))
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="Переход на страницу Контактов",
                attachment_type=allure.attachment_type.PNG
            )


