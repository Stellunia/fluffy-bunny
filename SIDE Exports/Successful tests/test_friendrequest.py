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

#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.service import Service as ChromeService
#service = ChromeService(executable_path=ChromeDriverManager().install())
#web_driver = webdriver.Chrome(service=service)

from helper_tests import simple_assert, boolean_assert

class TestFriendRequest():
  def setup_method(self, method):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    self.driver = webdriver.Chrome(chrome_options=chrome_options)
    #chrome_options.add_experimental_option("detach", True)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_friend_request(self):
    self.driver.get("https://www.webhallen.com/")
    
    try:
      print("Bypass cookies")
      element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/button[1]/span")))
      element.click()
    except:
      pass
  
    print("Accessing login")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Logga in")))
    element.click()
    
    print("Entering username")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//header[@id=\'main-header\']/div/div/div[3]/div/div[3]/form/div/div/div/input")))
    element.click()
    element.send_keys("EstelleTest2023")
    
    print("Entering password")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//header[@id=\'main-header\']/div/div/div[3]/div/div[3]/form/div/div/div[2]/input")))
    element.click()
    element.send_keys("testing1forEC")
    
    print("Logging in")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-child(1) > .text-btn > span")))
    element.click()
    
    print("Select Profile")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "EstelleTest2023")))
    element.click()
    
    print("Select friendslist")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Vänner")))
    element.click()
    
    print("Check friend requests")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/main/div/div[4]/div[1]/div/article/div[2]/div[2]/div[1]/button[2]/span[1]")))
    element.click()
    
    print("Accept friend request")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/main/div/div[4]/div[1]/div/article/div[2]/div[2]/div[2]/div/div[3]/span[2]")))
    element.click()
    
    self.driver.implicitly_wait(3)
    print("Return to friendslist")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Vänner")))
    element.click()
    
    print("Affirm friendship")
    friendship_check = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Stellunia")))
    simple_assert(friendship_check.text, "Stellunia")
    
    