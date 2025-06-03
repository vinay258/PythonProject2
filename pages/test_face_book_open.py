import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest_html

from conftest import vinay

email_text_xpath="//input[@name='email']"

def test_facebook_login(vinay):
   driver=vinay
   wait=WebDriverWait(driver,10)
   #email_ele=wait.until(ec.visibility_of_element_located((By.XPATH,email_text_xpath)))
   email_ele=driver.find_element(By.XPATH,email_text_xpath)
   print("iam giving the email")
   time.sleep(5)
   email_ele.send_keys("vinay@123")
   time.sleep(10)



