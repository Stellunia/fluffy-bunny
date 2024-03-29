# Generated by Selenium IDE
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
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

from helper_tests import simple_assert, boolean_assert

class TestLoginFunctions():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    self.driver = webdriver.Chrome(options=options)
    #chrome_options.add_experimental_option("detach", True)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("https://www.webhallen.com/")
    
    print("Accessing login")
    element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Logga in")))
    element.click()
    
    print("Entering username")
    element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//header[@id=\'main-header\']/div/div/div[3]/div/div[3]/form/div/div/div/input")))
    element.click()
    element.send_keys("EstelleTest2023")
    
    print("Entering password")
    element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//header[@id=\'main-header\']/div/div/div[3]/div/div[3]/form/div/div/div[2]/input")))
    element.click()
    element.send_keys("testing1forEC")
    
    print("Logging in")
    element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(1) > .text-btn > span")))
    element.click()
    
    login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main-header > div > div > div:nth-child(3) > div > label > div.member-logged-in-text > div.username > a")))
    simple_assert(login.text, "EstelleTest2023")
    
  
