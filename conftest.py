import pytest
import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker


@pytest.fixture(autouse=True, scope="class")
def driver(request):

    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    os.makedirs("logs", exist_ok=True)
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.handlers.clear()
    file_handler = logging.FileHandler("logs/tests.log", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

@pytest.fixture(scope="session")
def faker_ru():
    faker = Faker("ru_RU")
    return faker
