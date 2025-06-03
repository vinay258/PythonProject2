from pages.filling_form import FormPage


def test_form_submission(form_filling):
    driver = form_filling  #  your fixture
    form_page = FormPage(driver)  # Create object

    form_page.enter_first_name("Vinay")
    form_page.enter_last_name("Kumar")
    form_page.enter_address("123 Main St")
    form_page.enter_email("vinay@example.com")
    form_page.enter_phone_number("987654321")
    form_page.select_gender_male()
    form_page.select_cricket_hobby()
    form_page.select_movies_hobby()
    form_page.select_hockey_hobby()
    form_page.language_known()
    form_page.select_skill("C")
    form_page.country_known()
    form_page.enter_year("2000")
    form_page.enter_month("October")
    form_page.enter_day("7")
    form_page.enter_passwords("vinay@123")
    form_page.click_submit()
