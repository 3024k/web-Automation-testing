import unittest as U
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from random import randint
import random_numberGenerator

class Nagad_unitTest(U.TestCase):

    @classmethod
    def setUpClass(self) :
        self.driver = webdriver.Chrome(executable_path=r"C:/Users/Ashik/Downloads/chromedriver.exe")

    def setUp(self):
        pass

    def test_LOGIN_1(self):
        driver = self.driver
        driver.get("http://testing-ground.scraping.pro/login")
        time.sleep(1)
        driver.find_element_by_id("usr").send_keys("admin")
        driver.find_element_by_id("pwd").send_keys("12345")
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / form / input[3]').click()
        time.sleep(1)
        driver.find_element_by_class_name('success')
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / a').click()
        time.sleep(2)

    def test_LOGIN_2(self):
        driver = self.driver
        driver.find_element_by_id("usr").send_keys("admin")
        time.sleep(2)
        driver.find_element_by_id("pwd").send_keys(random_numberGenerator.random_with_N_digits(5))
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / form / input[3]').click()
        time.sleep(1)
        driver.find_element_by_class_name('error')
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / a').click()
        time.sleep(2)


    def test_LOGIN_3(self):
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_id("usr").send_keys(random_numberGenerator.id_generator())
        driver.find_element_by_id("pwd").send_keys("12345")
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / form / input[3]').click()
        time.sleep(1)
        driver.find_element_by_class_name('error')
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / a').click()
        time.sleep(2)

    def test_LOGIN_4(self):
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_id("usr").send_keys(random_numberGenerator.id_generator())
        driver.find_element_by_id("pwd").send_keys(random_numberGenerator.random_with_N_digits(5))
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / form / input[3]').click()
        time.sleep(1)
        driver.find_element_by_class_name('error')
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / a').click()
        time.sleep(2)

    def test_LOGIN_5(self):
        driver = self.driver
        time.sleep(2)
        driver.find_element_by_id("usr").send_keys("")
        driver.find_element_by_id("pwd").send_keys("")
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / form / input[3]').click()
        time.sleep(1)
        driver.find_element_by_class_name('error')
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / a').click()
        time.sleep(2)


    def test_LOGIN_6(self):
        driver = self.driver
        driver.find_element_by_id("usr").send_keys("admin")
        time.sleep(2)
        driver.find_element_by_id("pwd").send_keys("")
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / form / input[3]').click()
        time.sleep(1)
        driver.find_element_by_class_name('error')
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / a').click()
        time.sleep(2)

    def test_LOGIN_7(self):
        driver = self.driver
        driver.find_element_by_id("usr").send_keys("")
        time.sleep(2)
        driver.find_element_by_id("pwd").send_keys("12345")
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / form / input[3]').click()
        time.sleep(1)
        driver.find_element_by_class_name('error')
        time.sleep(2)
        driver.find_element_by_xpath('// *[ @ id = "case_login"] / a').click()
        time.sleep(2)


    def tearDown(self):
        #print("In TearDown Module")
        pass

    @classmethod
    def tearDownClass(self) :
        self.driver.close()

if __name__ == "__main__":
    U.main()