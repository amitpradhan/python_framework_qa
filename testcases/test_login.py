import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pageobjects.LoginPage import LoginPage
from selenium import webdriver
from utilities.read_properties import Read_Config
from utilities.Custom_Logger import Log_Gen


class Test_Login:
    app_url = Read_Config.get_app_ur()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    logger = Log_Gen.generate_log()

    # setup = webdriver.Chrome(ChromeDriverManager().install())

    def test_login(self, setup):
        self.logger.info("****************Test Login started..**************")
        self.logger.info("****************Verifyig Login test..**************")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        self.driver.get(self.app_url)
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_submit()
        page_title = self.driver.title
        current_url = self.driver.current_url
        if page_title == "Swag Labs" and current_url == "https://www.saucedemo.com/inventory.html":
            assert True
            self.driver.close()
            self.logger.info("**************** Login test passed.**************")
        else:
            self.driver.save_screenshot("..\\screenshot\\" + "test_login.png")
            self.driver.close()
            assert False
            self.logger.info("**************** Login test Failed.**************")

    def test_home_page_title(self, setup):
        self.logger.info("****************Test test_home_page_title started..**************")

        #   self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = setup
        self.driver.get(self.app_url)
        page_title = self.driver.title
        if page_title == "Swag Labs":
            assert True
            self.driver.close()
            self.logger.info("**************** test_home_page_title test passed.**************")
        else:
            self.driver.save_screenshot("..\\screenshot\\" + "test_home_page_title.png")
            self.driver.close()
            assert False
            self.logger.info("**************** test_home_page_title test failed.**************")
