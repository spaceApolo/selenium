import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class HelloWorld(unittest.TestCase):
    
    __driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
   #__driver = webdriver.Chrome(service = __service)

    @classmethod
    def setUpClass(self):
        self.__driver.implicitly_wait(10)

    def test_hello_world(self):
        self.__driver.get("https://www.platzi.com")
    
    def test_visit_wikipedia(self):
        self.__driver.get("https://www.wikipedia.org/")

    @classmethod
    def tearDownClass(self):
        self.__driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report'))
