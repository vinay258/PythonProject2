from pages.web_table_fill_and_read import Webpage

def test_add_row(web_table):
    driver = web_table  # your fixture
    web_page = Webpage(driver)  # Create object

    web_page.click_add_button()
    web_page.fill_name(
        firstname="vinay",
        lastname="kumar",
        email="vinay@gmail.com",
        age="28",
        salary="70000",
        department="Engineering"
    )