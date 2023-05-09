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

class TestFilterFunctions():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--window-size=1920,1080")
    self.driver = webdriver.Chrome(options=options)
    #chrome_options.add_experimental_option("detach", True)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_filterFunctions(self):
    self.driver.get("https://www.webhallen.com/")
    
    try:
      print("Bypass cookies")
      element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[3]/div/div/button[1]/span")))
      element.click()
    except:
      pass
    
    print("Open Category")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Datorer & Tillbehör")))
    element.click()
    
    print("Select subcategory")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Gamingtillbehör")))
    element.click()
    
    print("Selecting sub-subcategory")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Rattar")))
    element.click()
    
    print("Clear price field and enter specified number")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.NAME, "price")))
    element.send_keys(Keys.CONTROL + "a")
    element.send_keys(Keys.DELETE)
    element.send_keys("500")
    
    print("Filter checkbox 'Webblager'")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-child(2) > .checkbox-wrap:nth-child(2) > .checkbox")))
    element.click()
    
    print("Change filter format to descriptive list")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".toggle-btn:nth-child(1) > .toggle-icon:nth-child(1) > img")))
    element.click()
    
    self.driver.implicitly_wait(3)
    print("Change filter format to pictures")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/main/div/div[4]/div[1]/div/article/div[4]/div[1]/div[2]/button[3]/span/img")))
    element.click() 
    
    print("Wait and then scroll")
    self.driver.implicitly_wait(3)
    self.driver.execute_script("window.scrollBy(0,500)","")
    
    #print("Expand checkboxes")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-list-filter-container > div.product-list-filters > div > div:nth-child(5) > div:nth-child(2) > div > a")))
    #element.click()
    
    self.driver.implicitly_wait(3)
    print("Filter checkbox 'Thrustmaster'")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-child(1) > .checkbox-wrap:nth-child(2) > .checkbox")))
    element.click()
    
    print("Search for a specific product")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".input-field")))
    element.send_keys("TH8A")
    
    print("Select specified product")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Thrustmaster TH8A Add-On Shifter")))
    element.click()
    
    #print("")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Rattar")))
    #element.click()
    
    #
    #print("")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Gå till toppen av sidan")))
    #element.click()
    
    print("Navigate to a category")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "TV, Ljud & Bild")))
    element.click()
    
    print("Navigate to a category")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Studio, Instrument & DJ")))
    element.click()
    
    print("Filter with checkbox ''")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-child(1) > .checkbox-wrap:nth-child(2) > .checkbox")))
    element.click()
    
    print("Select a specific product")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Mackie MC-250")))
    element.click()
    
    print("Navigate to a category")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Spel")))
    element.click()
    
    print("")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-child(4) .popular-categories-title")))
    element.click()
    
    print("Select a specific product")
    element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "Nintendo Switch OLED Model Neon Red/Neon Blue")))
    element.click()
    
    self.driver.implicitly_wait(3)
    print("Assert we've reached the last page by checking the product header")
    header_name = self.driver.find_element(By.CSS_SELECTOR, "#main-container > div.product-page-wrapper.child-view > div.product-wrapper > div > article > header > div.px-5.col-xs-12 > h1")
    simple_assert(header_name.text, "Nintendo Switch OLED Model Neon Red/Neon Blue")
    
    #Tests below appeared to work twice, then never worked again - cannot figure out why or what causes them to fail and/or work
    #print("Expand drop-down menu of colour choices")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".variant-selector > .dropdown-label > span")))
    #element.click()
    
    #print("Switch colour of specified product")
    #element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-list-variant-item:nth-child(1) .small")))
    #element.click()
    
    #self.driver.implicitly_wait(3)
    #print("Assert we've reached the last page by checking the product header")
    #header_name = self.driver.find_element(By.CSS_SELECTOR, "#main-container > div.product-page-wrapper.child-view > div.product-wrapper > div > article > header > div.px-5.col-xs-12 > h1")
    #simple_assert(header_name.text, "Nintendo Switch OLED Model White")


