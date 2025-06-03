from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC

from pages.filling_form import first_name_xpath

add_button_xpath="//button[@type='button' and contains(text(),'Add')]"
first_name="//input[@id='firstName']"
last_name="//input[@id='lastName']"
email_input="//input[@id='userEmail']"
age_input="//input[@id='age']"
salary_input="//input[@id='salary']"
department_input="//input[@id='department']"
submit_input="//button[@id='submit']"




class Webpage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def click_add_button(self):
        add_button = self.driver.find_element(By.XPATH,add_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_button)
        add_button.click()

    def fill_name(self,firstname,lastname,email,age,salary,department):
        firstname = str(firstname)
        lastname = str(lastname)
        email = str(email)
        age = str(age)
        salary = str(salary)
        department = str(department)
        self.driver.find_element(By.XPATH,first_name_xpath).send_keys(firstname)
        self.driver.find_element(By.XPATH,first_name_xpath).send_keys(lastname)
        self.driver.find_element(By.XPATH,email_input).send_keys(email)
        self.driver.find_element(By.XPATH,age_input).send_keys(age)
        self.driver.find_element(By.XPATH,salary_input).send_keys(salary)
        self.driver.find_element(By.XPATH,department_input).send_keys(department)
        self.driver.find_element(By.XPATH,submit_input).click()


