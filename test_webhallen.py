from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
# import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.wait import WebDriverWait
from helper_tests import simple_assert, boolean_assert

WEBHALLEN_SITE = "https://www.webhallen.com/"

@pytest.fixture
def load_driver():

    # Selenium 4.6 and above use a BETA version of Selenium Manager which automatically handles the browser drivers
    # If we have an older version, or if Selenium Managers somehow does not work on your system, follow this guide for installing the correct driver:
    # https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

    driver = webdriver.Chrome()

    # NOT THE BEST SOLUTION BUT USE IT AS A PLACEHOLDER
    # WARNING: THIS DOES NOT WORK WITH EXPLICIT WAIT
    # driver.implicitly_wait(5)

    yield driver

    driver.quit()
    
def test_webhallen_nav(load_driver):
    
    driver = load_driver
    driver.get(WEBHALLEN_SITE)
    
    search_bar = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/div/header/div/div/div[2]/div/div/div/input") #input.form-control
    search_button = driver.find_element(By.CLASS_NAME, "search-button")
    
    search_bar.send_keys("Nvidia")
    search_button.click()
    wait = WebDriverWait(driver, 5)
    
    select_product = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[1]/div[1]/div[2]/div/header/div/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[1]/a/div/div")
    select_product.click()
    
    