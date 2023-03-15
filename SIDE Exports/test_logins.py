import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFilterFunctions():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_filterFunctions(self):
    self.driver.get("https://www.webhallen.com/")
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div/header/div/div/div[3]/div/div/div[1]/img").click()
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div/header/div/div/div[3]/div/div[3]/form/div/div/div[1]/label").send_keys("Stellunia")
    self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div/header/div/div/div[3]/div/div[3]/form/div/div/div[2]/input").send_keys("FU74N4R1a.")
    self.driver.find_element(By.LINK_TEXT, "Logga in").click()
    self.driver.find_element(By.LINK_TEXT, "Stellunia")