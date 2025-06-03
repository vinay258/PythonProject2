from pages.filling_form import FormPage



# Setting up the form for submission
def test_form_submission(form_filling):
    driver = form_filling  # your fixture
    form_page = FormPage(driver)  # Create object

    # Filling in the form with test data
    form_page.enter_first_name("Vinay")  # Entering first name
    form_page.enter_last_name("Kumar")  # Entering last name
    form_page.enter_address("123 Main St")  # Entering address
    form_page.enter_email("vinay@example.com")  # Entering email
    form_page.enter_phone_number("987654321")  # Entering phone number
    form_page.select_gender_male()  # Selecting gender: Male
    form_page.select_cricket_hobby()  # Selecting hobby: Cricket
    form_page.select_movies_hobby()  # Selecting hobby: Movies
    form_page.select_hockey_hobby()  # Selecting hobby: Hockey
    form_page.language_known()  # Selecting known language(s)
    form_page.select_skill("C")  # Selecting skill: C
    form_page.country_known()  # Selecting country information
    form_page.enter_year("2000")  # Entering year
    form_page.enter_month("October")  # Entering month
    form_page.enter_day("7")  # Entering day
    form_page.enter_passwords("vinay@123")  # Entering password
    form_page.click_submit()  # Clicking submit button
