import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class HelloWorld(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path ='./drivers/chromedriver')
        #browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
        driver = self.driver
        driver.implicity_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')
    
    def test_visit_wikipedia(self):
        self.driver.get('www.google.com')


    def tearDown(self) -> None:
        self.driver.quit() 

    if __name__ == '__main__':
        unittest.main(verbosity=2, testRunner= HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))