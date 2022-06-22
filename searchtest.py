import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class HomePageTest(unittest.TestCase):

    #__driver = webdriver.Chrome(executable_path="./drivers/chromedriver")


    @classmethod
    def setUpClass(self):
        
        
        self.driver = webdriver.Chrome(executable_path="./drivers/chromedriver")
        #self.__driver.get('https://www.google.com')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()



    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID,'search')
        #self.driver.get("https://www.google.com")

    @classmethod
    def tearDownClass(self):
        self.__driver.quit()
    
if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report'))

    #unittest.main(verbosity=2)