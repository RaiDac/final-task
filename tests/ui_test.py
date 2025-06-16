import pytest
from selenium.webdriver.chrome.options import Options
from testui.support.appium_driver import NewDriver, TestUIDriver
from cv_pom.frameworks import TestUICVPOMDriver
from cv_pom.cv_pom_driver import CVPOMDriver
from testui.elements.testui_element import e
from tests.pages.landing_page import LandingPage
from pathlib import Path


@pytest.fixture(autouse=True)
def testui_driver():
    options = Options()
    options.add_argument("disable-user-media-security")
    options.add_argument("--force-device-scale-factor=1")
    options.add_argument("--headless")
    driver = NewDriver().set_logger().set_selenium_driver(chrome_options=options)

    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def cv_pom_driver(testui_driver):
    BASE_DIR = Path(__file__).resolve().parent
    model_path = BASE_DIR / "resources" / "best_g.pt" 
    driver = TestUICVPOMDriver(model_path, testui_driver)
    yield driver


class TestSuite:
    def test_for_chililabs(self, testui_driver: TestUIDriver, cv_pom_driver: CVPOMDriver):
        landing_page = LandingPage(testui_driver, cv_pom_driver)
        testui_driver.navigate_to("https://chililabs.io")
        testui_driver.get_driver().set_window_size(1200, 700)
        landing_page.accept_cookies().go_to_contact_us().fill_all_form_details()


    def test_for_chililabs_cv(self, testui_driver: TestUIDriver, cv_pom_driver: CVPOMDriver):
        testui_driver.navigate_to("https://chililabs.io")
        testui_driver.get_driver().set_window_size(1200, 700)
        landing_page = LandingPage(testui_driver, cv_pom_driver)
        landing_page.accept_cookies_cv().go_to_contact_us_cv().fill_all_form_details_cv()
