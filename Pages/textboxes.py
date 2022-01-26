from selenium.webdriver.common.by import By


class textboxes:
    def __init__(self,driver):
        self.driver = driver
        self.fullname_ID = "userName"
        self.email = "userEmail"
        self.c_address = "currentAddress"
        self.p_address = "permanentAddress"
        self.submit_btn = "submit"

    def enter_fullname(self,name):
        self.driver.find_element(By.ID,self.fullname_ID).send_keys(name)

    def enter_email(self,mail):
        self.driver.find_element(By.ID, self.email).send_keys(mail)

    def enter_address(self,caddress):
        self.driver.find_element(By.ID, self.c_address).send_keys(caddress)

    def enter_perm_address(self,paddress):
        self.driver.find_element(By.ID, self.p_address).send_keys(paddress)

    def click_submit(self):
        self.driver.find_element(By.ID,self.submit_btn).click()

