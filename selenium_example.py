from selenium import webdriver
from locators import locator
from csv import reader
import random
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.Edge import EdgeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

#driver = webdriver.Edge(executable_path = '.\\msedgedriver.exe')
driver.implicitly_wait(10)

driver.get("http://automationpractice.com/")
driver.maximize_window()

with open('data.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=',')
    for row in csvreader:

        assert driver.find_element(*locator["contactUs_button"]).is_displayed()
        driver.find_element(*locator["contactUs_button"]).click()

        assert driver.title == "Contact us - My Store"
        select = Select(driver.find_element(*locator["subjectHeading_select"])).select_by_value("2")

        assert driver.find_element(*locator["email_field"]).is_displayed()
        driver.find_element(*locator["email_field"]).send_keys(row[0])

        assert driver.find_element(*locator["orderReference_field"]).is_displayed()
        driver.find_element(*locator["orderReference_field"]).send_keys(row[1])
        
        assert driver.find_element(*locator["message_field"]).is_displayed()
        driver.find_element(*locator["message_field"]).send_keys(row[2])

        assert driver.find_element(*locator["send_button"]).is_displayed()
        driver.find_element(*locator["send_button"]).click()

        assert driver.find_element(*locator["alertMessage_text"]).is_displayed()

        assert driver.find_element(*locator["home_button"]).is_displayed()
        driver.find_element(*locator["home_button"]).click()
driver.quit()


























