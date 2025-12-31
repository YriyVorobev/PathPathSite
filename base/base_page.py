import allure
import logging
from faker import Faker
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from metaclasses.meta_locator import MetaLocator


class BasePage(metaclass=MetaLocator):

    _MY_INFO_ITEM = "//a/span[text()='My Info']"


    def __init__(self,driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.action = ActionChains(self.driver)
        self.faker = Faker()
        self.log = logging.getLogger(self.__class__.__name__)

    def open(self):
        with allure.step(f"Open {self._PAGE_URL} page"):
            self.driver.get(self._PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self._PAGE_URL))

    def go_to_my_info_page(self):
        self.wait.until(EC.element_to_be_clickable(self._MY_INFO_ITEM)).click()

