import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import logging




first_name_xpath=(By.XPATH,"//input[@placeholder='First Name']")
last_name_xpath="//input[@placeholder='Last Name']"
address_xpath="//textarea[@rows='3']"
email_xpath="//input[@type='email']"
phone_number_xpath="//input[@type='tel']"
Male_radio_button_xpath="//input[@type='radio' and @value='Male']"
Female_radio_button_xpath="//input[@type='radio' and @value='FeMale']"
cricket_radio_button_xpath="//input[@type='checkbox' and @value='Cricket']"
Movies_radio_button_xpath="//input[@type='checkbox' and @value='Movies']"
Hockey_radio_button_xpath="//input[@type='checkbox' and @value='Hockey']"
Language_xpath="//div[@id='msdd']"
skills_xpath="//select[@type='text' and @id='Skills']"
country_xpath="//span[@role='combobox']"
year_xpath="//select[@id='yearbox']"
month_xpath="//select[@placeholder='Month']"
Day_xpath="//select[@placeholder='Day']"
password_xpath="//input[@id='firstpassword']"
confirm_password_xpath="//input[@id='secondpassword']"
submit_button="//button[@id='submitbtn']"



class FormPage:
    """
    This class encapsulates the methods and elements of a web form page.
    It uses Selenium's WebDriverWait to interact with elements on the page.
    """

    def __init__(self, driver):
        """
        Initializes the form page with the WebDriver instance.
        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.file_handler = logging.FileHandler("C:\\Users\\vinay\\PycharmProjects\\PythonProject2\\Logs1")
        self.logger.addHandler(self.file_handler)


    def enter_first_name(self, name):
        """
        Enters the given first name into the 'First Name' input field.
        :param name: String containing the first name.
        """
        self.logger.info(f"Entering first name: {name}")
        (self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']")))
         .send_keys(name))
        time.sleep(3)

    def enter_last_name(self, name):
        """
        Enters the given last name into the 'Last Name' input field.
        :param name: String containing the last name.
        """
        self.logger.info(f"Entering last name: {name}")
        (self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Last Name']")))
         .send_keys(name))
        time.sleep(3)

    def enter_address(self, address):
        """
        Enters the given address into the 'Address' textarea.
        :param address:
        :return:
        """
        self.logger.info(f"Entering address: {address}")
        (self.wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@rows='3']")))
         .send_keys(address))
        time.sleep(3)

    def enter_email(self, email):
        """
        Enters the given email into the 'Email' input field.
        :param email: String containing the email address.
        """
        self.logger.info(f"Entering email: {email}")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys(email)
        time.sleep(3)

    def enter_phone_number(self, phone_number):
        """
        Enters the given phone number into the 'Phone Number' input field.
        :param phone_number: String containing the phone number.
        """
        self.logger.info(f"Entering phone number: {phone_number}")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='tel']"))).send_keys(phone_number)
        time.sleep(3)

    def select_gender_male(self):
        """
        Selects the 'Male' gender radio button.
        """
        self.logger.info("Selecting gender: Male")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='Male']"))).click()
        time.sleep(3)

    def select_gender_female(self):
        """
        Selects the 'Female' gender radio button.
        """
        self.logger.info("Selecting gender: Female")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @value='FeMale']"))).click()
        time.sleep(3)

    def select_cricket_hobby(self):
        """
        Selects the 'Cricket' hobby checkbox.
        """
        self.logger.info("Selecting hobby: Cricket")
        (self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @value='Cricket']")))
         .click())
        time.sleep(3)

    def select_movies_hobby(self):
        """
        Selects the 'Movies' hobby checkbox.
        """
        self.logger.info("Selecting hobby: Movies")
        (self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @value='Movies']")))
         .click())
        time.sleep(3)

    def select_hockey_hobby(self):
        """
        Selects the 'Hockey' hobby checkbox.
        """
        self.logger.info("Selecting hobby: Hockey")
        (self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @value='Hockey']")))
         .click())
        time.sleep(3)

    def language_known(self):
        """
        Selects 'English' from the language dropdown menu.
        """
        self.logger.info("Selecting language: English")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='msdd']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='English']"))).click()
        time.sleep(3)

    def select_skill(self, skill_name):
        """
        Selects the given skill from the skill dropdown menu.
        """
        self.logger.info(f"Selecting skill: {skill_name}")
        skill_dropdown = Select(self.wait.until(EC.presence_of_element_located
                                                ((By.XPATH, "//select[@type='text' and @id='Skills']"))))
        skill_dropdown.select_by_visible_text(skill_name)
        time.sleep(3)

    def country_known(self):
        """
        Selects 'India' from the country dropdown menu.
        """
        self.logger.info("Selecting country: India")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@role='combobox']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text()='India']"))).click()
        time.sleep(3)

    def enter_year(self, year):
        """
        Selects the year from the year dropdown menu.
        :param year: The year to select.
        """
        self.logger.info(f"Selecting year: {year}")
        dropdown = Select(self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@id='yearbox']"))))
        dropdown.select_by_visible_text(year)
        time.sleep(2)

    def enter_month(self, month):
        """
        Selects the month from the month dropdown menu.
        :param month: The month to select.
        """
        self.logger.info(f"Selecting month: {month}")
        dropdown = Select(self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@placeholder='Month']"))))
        dropdown.select_by_visible_text(month)
        time.sleep(2)

    def enter_day(self, day):
        """
        Selects the day from the day dropdown menu.
        :param day: The day to select.
        """
        self.logger.info(f"Selecting day: {day}")
        dropdown = Select(self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@placeholder='Day']"))))
        dropdown.select_by_visible_text(day)
        time.sleep(2)

    def enter_passwords(self, password):
        """
        Enters the given password into the password and confirm password fields.
        :param password: The password to enter.
        """
        self.logger.info("Entering passwords")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='firstpassword']"))).send_keys(password)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='secondpassword']"))).send_keys(password)
        time.sleep(3)

    def click_submit(self):
        """
        Clicks the 'Submit' button to submit the form.
        """
        self.logger.info("Clicking the submit button")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='submitbtn']"))).click()
        time.sleep(3)