from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class HerokuTableReader:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # These XPaths point to table1
        self.rows_xpath = "//table[@id='table1']//tr"
        self.columns_xpath = "//table[@id='table1']//th"
        self.cell_xpath= "//table[@id='table1']//tr[{}]//td[{}]"

    def read_table(self):
        rows = self.driver.find_elements(By.XPATH, self.rows_xpath)
        columns = self.driver.find_elements(By.XPATH, self.columns_xpath)

        no_of_rows = len(rows)
        no_of_columns = len(columns)

        print("Table1 - Row count:", no_of_rows)
        print("Table1 - Column count:", no_of_columns)

        for row in range(1, no_of_rows):
            print(f"Row {row} data:")
            for col in range(1, no_of_columns + 1):
                req_cell_xpath = self.cell_xpath.format(row, col)
                cell = self.driver.find_element(By.XPATH, req_cell_xpath)
                time.sleep(0.2)  # for readable output
                print(cell.text, end=" | ")
            print()

        print("Finished reading table1.")
