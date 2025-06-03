import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from conftest import form_filling




first_name_xpath="//input[@placeholder='First Name']"
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





def test_form_filling_data(form_filling):
    driver = form_filling
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)

    first_name_ele = wait.until(EC.visibility_of_element_located((By.XPATH, first_name_xpath)))
    # here we can give the input
    first_name_ele.send_keys("vinay")
    time.sleep(5)

    last_name_ele = wait.until(EC.visibility_of_element_located((By.XPATH, last_name_xpath)))
    # here we can give the input
    last_name_ele.send_keys("kumar")
    time.sleep(5)

    address_ele = wait.until(EC.visibility_of_element_located((By.XPATH, address_xpath)))
    # here we can give the text input
    address_ele.send_keys("3/70c,paipalli,puttaparthi")
    time.sleep(5)

    email_ele = wait.until(EC.visibility_of_element_located((By.XPATH, email_xpath)))
    # here we can give the input
    email_ele.send_keys("vinay@example.com")
    time.sleep(5)

    phone_number_ele = wait.until(EC.visibility_of_element_located((By.XPATH, phone_number_xpath)))
    # here we can input text for phone number
    phone_number_ele.send_keys("9876543210")
    time.sleep(5)

    female_radio_button_ele = wait.until(EC.element_to_be_clickable((By.XPATH, Female_radio_button_xpath)))
    # here we can click the female radio button
    female_radio_button_ele.click()  # optional if Male selected
    time.sleep(5)

    male_radio_button_ele = wait.until(EC.element_to_be_clickable((By.XPATH, Male_radio_button_xpath)))
    # here we can click the radio button
    male_radio_button_ele.click()
    time.sleep(5)

    movies_radio_button_ele = wait.until(EC.element_to_be_clickable((By.XPATH, Movies_radio_button_xpath)))
    # here we can click the movies radio button
    movies_radio_button_ele.click()
    time.sleep(5)

    cricket_radio_button_ele = wait.until(EC.element_to_be_clickable((By.XPATH, cricket_radio_button_xpath)))
    # here we can click the cricket radio button
    cricket_radio_button_ele.click()
    time.sleep(5)

    hockey_radio_button_ele = wait.until(EC.element_to_be_clickable((By.XPATH, Hockey_radio_button_xpath)))
    # here we can select the hockey
    hockey_radio_button_ele.click()
    time.sleep(5)

    language_ele = wait.until(EC.element_to_be_clickable((By.XPATH, Language_xpath)))
    # here we can give the input text
    language_ele.click()
    language_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='English']")))
    language_option.click()
    time.sleep(5)

    skills_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, skills_xpath))))
    skills_dropdown.select_by_index(5)
    time.sleep(5)

    country_ele = wait.until(EC.element_to_be_clickable((By.XPATH, country_xpath)))
    # here we can use action chains to enter and press enter
    country_ele.click()
    country_options=wait.until(EC.element_to_be_clickable((By.XPATH,"//li[text()='India']")))
    country_options.click()
    time.sleep(5)

    year_ele= Select(wait.until(EC.element_to_be_clickable((By.XPATH,year_xpath))))
    year_ele.select_by_value("2000")
    time.sleep(5)

    month_ele= Select(wait.until(EC.element_to_be_clickable((By.XPATH, month_xpath))))
    month_ele.select_by_visible_text("October")
    time.sleep(5)

    day_ele = Select(wait.until(EC.element_to_be_clickable((By.XPATH, Day_xpath))))
    day_ele.select_by_value("7")
    time.sleep(5)

    password_ele=wait.until(EC.element_to_be_clickable((By.XPATH, password_xpath)))
    password_ele.send_keys("vinay@123")
    time.sleep(5)

    confirm_password_ele = wait.until(EC.element_to_be_clickable((By.XPATH, confirm_password_xpath)))
    confirm_password_ele.send_keys("vinay@123")
    time.sleep(8)

    submit_button_ele = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button)))
    submit_button_ele.send_keys("vinay@123")
    time.sleep(5)







