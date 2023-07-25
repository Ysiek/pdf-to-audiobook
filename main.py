import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org/")
        self.assertIn("Python", driver.title)
        input = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/div[1]/div/form/fieldset/input')
        input.send_keys('wpisz tu coś')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
