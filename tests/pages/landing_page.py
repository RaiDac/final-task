from testui.elements.testui_element import e
from tests.pages.contact_us import ContactUs

class LandingPage:
    def __init__(self, driver, cv_driver):
        self.driver = driver
        self.cv_driver = cv_driver
        self.contact_us_button = e(driver, "css", "a[href='/contact-us']")
        self.accept_cookies_button = e(driver, "css", "._styled__StyledButton-sc-208d1564-2.gCaqQM")
        # CV elements
        self.contact_us_button_cv = cv_driver.element({"label": "contact-us-button"})
        self.accept_cookies_button_cv = cv_driver.element({"label": "all-cookies-button"})

    def accept_cookies(self):
        self.assert_text("Accept All", self.accept_cookies_button.get_text())
        self.accept_cookies_button.click()
        return self

    def accept_cookies_cv(self):
        self.accept_cookies_button_cv.click()
        return self

    def go_to_contact_us(self):
        self.assert_text("Contact us", self.contact_us_button.get_text())
        self.contact_us_button.click()
        return ContactUs(self.driver, self.cv_driver)

    def go_to_contact_us_cv(self):
        self.contact_us_button_cv.click()
        return ContactUs(self.driver, self.cv_driver)

    @staticmethod
    def assert_text(expected, actual):
        assert expected == actual, f"Expected {expected}, but got {actual}"