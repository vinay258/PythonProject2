import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import pytest
import pytest_html
from  conftest import vinay,vinaykumar


drop_down="//a[contains(text(),'SwitchTo')]"
title="//h1[contains(text(),'Automation Demo Site')]"
alerts="//a[contains(text(),'Alerts')]"
windows="//a[contains(text(),'Windows')]"
alert_and_text="//a[contains(text(),'Alert with Textbox')]"
click_button="//button[contains(text(),'click the button to demonstrate the prompt box')]"
new_seperate_button="//a[contains(text(),'Open New Seperate Windows')]"
click_on_new_window="//button[@onclick='newwindow()']"
title_new_window="//title[contains(text(),'Selenium')]"
new_tabbed_window="//a[contains(text(),'Open New Tabbed Windows')]"
click_button_for_new_tab="//a[@target='_blank' and @href='http://www.selenium.dev']"


def test_demo_site_page(vinaykumar):
    driver=vinaykumar
    wait=WebDriverWait(driver,10)
    action=ActionChains(driver)
    drop_down_ele=wait.until(ec.presence_of_element_located((By.XPATH,drop_down)))
    action.move_to_element(drop_down_ele).perform()
    time.sleep(5)
    print("iam clicking the alerts")
    ele=driver.find_element(By.XPATH,alerts).click()
    print("clicking on the alert and textbox ")
    text_ele=wait.until(ec.visibility_of_element_located((By.XPATH,alert_and_text)))
    text_ele.click()
    time.sleep(4)
    click_ele=driver.find_element(By.XPATH,click_button)
    click_ele.click()
    time.sleep(4)
    print("switching into the alert text box")
    alert = driver.switch_to.alert
    alert.send_keys("vinay kumar")
    time.sleep(2)
    alert.accept()
    time.sleep(5)
    print("moving to the next element")
    drop_down_ele = wait.until(ec.presence_of_element_located((By.XPATH, drop_down)))
    action.move_to_element(drop_down_ele).perform()
    time.sleep(5)
    print("iam clicking the windows")
    time.sleep(5)
    driver.find_element(By.XPATH, windows).click()
    print("clicking on the windows")
    windows_clck_button=driver.find_element(By.XPATH,new_seperate_button)
    print("selecting the multiple windows")
    time.sleep(2)
    print("clicking open multiple windows")
    windows_clck_button.click()
    time.sleep(5)
    click_on_multiple_window_ele=driver.find_element(By.XPATH,click_on_new_window)
    click_on_multiple_window_ele.click()
    driver.maximize_window()
    time.sleep(5)
    print("iam opening the new tab")
    new_window_tab_ele=driver.find_element(By.XPATH,new_tabbed_window)
    new_window_tab_ele.click()

    print("clicking on new tab")
    main_window = driver.current_window_handle
    click_button_for_new_tab_ele = driver.find_element(By.XPATH, click_button_for_new_tab)
    click_button_for_new_tab_ele.click()
    time.sleep(8)

    # Get all window handles
    all_windows = driver.window_handles
    print("Total windows opened:", len(all_windows))

    # Switch to the main window
    for window in all_windows:
        if window != main_window:
            driver.switch_to.window(main_window)
            print("Switched to main window.")
            print("Title of main window:", driver.title)
            assert "Frames & windows" in driver.title
            time.sleep(5)
            break  # Stay in the new window without closing it

    # Now switch back to new window
    driver.switch_to.window(all_windows[1])
    time.sleep(5)
    print("Switched back to new window.")
    print("New window title:", driver.title)





