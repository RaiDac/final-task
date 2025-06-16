from testui.elements.testui_element import e

class ContactUs:
    def __init__(self, driver, cv_driver):
        self.name_field = e(driver, "css", "input[name='name']")
        self.email_field = e(driver, "css", "input[name='email']")
        self.message = e(driver, "css", "textarea[name='message']")
        # CV elements
        self.name_field_cv = cv_driver.element({"label": "name-box"})
        self.email_field_cv = cv_driver.element({"label": "email-box"})
        self.message_cv = cv_driver.element({"label": "message-box"})

    def fill_all_form_details(self):
        self.name_field.send_keys("John Doe")
        self.email_field.send_keys("johndoe@example.com")
        self.message.send_keys("This is a test message")

    def fill_all_form_details_cv(self):
        self.name_field_cv.send_keys("John Doe")
        self.email_field_cv.swipe_to("down").send_keys("johndoe@example.com")
        self.message_cv.swipe_to("down").send_keys("This is a test message")