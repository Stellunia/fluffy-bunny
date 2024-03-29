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

class TestCartFunctions():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    self.driver = webdriver.Chrome(options=options)
    #chrome_options.add_experimental_option("detach", True)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cartFunctions(self):
    self.driver.get("https://www.webhallen.com/")
    #self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[2]/div/nav/div/ul/li[4]/a").click()
    
    try:
      print("Bypass cookies")
      element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/button[1]/span")))
      element.click()
    except:
      pass
    
    #Layout
    #print("Title")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By. , )))
    #element.click() / #element.send_keys("")
    
    print("Access Datorkomponenter")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Datorkomponenter")))
    element.click() #element.send_keys("")
    
    print("Access RAM-Minne category")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "RAM-minne")))
    element.click()
    
    print("Search for specific product")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/main/div/div[4]/aside/div[2]/div/div[2]/div/div[1]/div[2]/div/input")))
    element.send_keys("Corsair Vengeance RGB PRO SL 32GB (2x16GB)")
    
    #WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".filter-box:nth-child(1) h3")))
    #self.driver.find_element(By.XPATH, "(//input[@type=\'text\'])[2]").send_keys("Hyte Y60")
    
    self.driver.implicitly_wait(3)

    print("Select specified product")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT , "Corsair Vengeance RGB PRO SL 32GB (2x16GB)")))
    element.click()
    
    #print("Wait and then scroll")
    self.driver.implicitly_wait(3)
    #self.driver.execute_script("window.scrollBy(0,500)","")
    
    #print("Add a package deal to cart")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/main/div/div[4]/div[1]/div/div[2]/div[1]/div/article/div/section/div[1]/button/span")))
    #element.click()
    
    #try:
      #print("Close login window")
      #element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/header/div/div/div[3]/div/div[3]/button")))
      #element.click()
    #except:
      #pass
    
    #Deprecated
    #print("Wait and scroll back")
    #WebDriverWait(self.driver,3)
    #self.driver.execute_script("window.scrollBy(0,500)","")
    
    #Deprecated
    #print("Wait and scroll back")
    #WebDriverWait(self.driver, 3)
    #self.driver.execute_script("window.scrollBy(0,-500)","")
    
    #print("Open cart")
    #element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/header/div/div/div[4]/div/label/div")))
    #element.click() #By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/header/div/div/div[4]/div/label/div/div[2]/strong"
    
    #self.driver.implicitly_wait(3)
    #print("Removal of first product in cart")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-list-row:nth-child(1) .btn-remove-item > .icon")))
    #element.click()
    
    #self.driver.implicitly_wait(3)
    #print("Removal of second product in cart")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-list-row:nth-child(2) .btn-remove-item > .icon")))
    #element.click()
    
    #self.driver.implicitly_wait(3)
    #print("Removal of first product in cart")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-list-row:nth-child(1) .btn-remove-item > .icon")))
    #element.click()

    #self.driver.implicitly_wait(3)
    #print("Close cart window")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-close > .icon")))
    #element.click()
    
    print("Add the product to cart")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/main/div/div[4]/div[1]/div/div[2]/div[1]/div/article/div/div[1]/div/section[2]/div[1]/button/span")))
    element.click()
    
    self.driver.implicitly_wait(3)
    try: 
      print("Deny buyer protection")
      element = WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[4]/div/div/div[4]/button[2]")))
      element.click()
    except:
      pass
    
    self.driver.implicitly_wait(3)
    print("Open cart")
    element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/header/div/div/div[4]/div/label/div")))
    element.click()
    
    self.driver.implicitly_wait(3)
    print("To the cart page")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[2]/div/header/div/div/div[4]/div/div[2]/div/div[3]/a")))
    element.click()
    
    self.driver.implicitly_wait(3)
    print("Assert the product is in the cart")
    product_in_cart = self.driver.find_element(By.XPATH, "//div[@id='main-container']/div[2]/div[2]/div/ul/li/div/div/span/a")
    simple_assert(product_in_cart.text, "Corsair Vengeance RGB PRO SL 32GB (2x16GB) / 3600MHz / DDR4 / CL18 / CMH32GX4M2D3600C18")
    
    #print("Navigate to Köpvillkor page")
    #element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Köpvillkor")))
    #element.click()
  
    #print("Assert we've reached the last page")
    #title_name = self.driver.find_element(By.CSS_SELECTOR, "#main-container > article > section.info-top.d-flex.flex-wrap > div > h1")
    #simple_assert(title_name.text, "Köpvillkor")
