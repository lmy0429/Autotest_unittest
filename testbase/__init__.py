from selenium import webdriver
import unittest


class SAE(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1366,780)

    def tearDown(self):
        self.driver.quit()
