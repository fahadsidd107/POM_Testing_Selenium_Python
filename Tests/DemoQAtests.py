import time
import unittest
from Pages.textboxes import textboxes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DemoQaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://demoqa.com/text-box")
        cls.driver.maximize_window()

    def test_filltextboxes(self):
        driver = self.driver
        text = textboxes(driver)
        text.enter_fullname("Fahad Siddiqui")
        text.enter_email("fsiddiqui107@gmail.com")
        text.enter_address("Liaquatabad")
        text.enter_perm_address("Karachi")
        text.click_submit()
        time.sleep(0.1)

    def test_practiceform(self):
        @classmethod
        def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()
