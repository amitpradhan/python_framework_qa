from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:

    textbox_username_id = "user-name"
    textbox_password_id = "password"
    btn_submit_id = "login-button"

    def __init__(self, driver):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.chrome
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, pwd):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(pwd)

    def click_submit(self):
        self.driver.find_element(By.ID, self.btn_submit_id).click()

