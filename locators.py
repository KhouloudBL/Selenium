from selenium.webdriver.common.by import By

locator = {
    "contactUs_button": (By.ID, "contact-link"),
    "subjectHeading_select": (By.ID, "id_contact"),
    "email_field": (By.ID, "email"),
    "orderReference_field": (By.ID, "id_order"),
    "message_field": (By.ID, "message"),
    "send_button": (By.ID, "submitMessage"),
    "alertMessage_text": (By.XPATH, "//*[text()='Your message has been successfully sent to our team.']"),
    "home_button": (By.XPATH, "/html/body/div/div[2]/div/div[3]/div/ul/li/a"),
}
