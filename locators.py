from selenium.webdriver.common.by import By

locator = {
    "contact_button": (By.ID, "contact-link"),
    "subject_Heading": (By.ID, "id_contact"),
    "email_field": (By.ID, "email"),
    "order_Reference": (By.ID, "id_order"),
    "message": (By.ID, "message"),
    "send_button": (By.ID, "submitMessage"),
    "alertMessage_text": (By.XPATH, "//*[text()='Your message has been successfully sent to our team.']"),
    "home_button": (By.XPATH, "/html/body/div/div[2]/div/div[3]/div/ul/li/a"),
}
