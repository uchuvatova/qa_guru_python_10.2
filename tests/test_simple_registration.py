from demoqa_tests.data.users import User, Gender
from demoqa_tests.pages.shortRegistrationPage import ShortRegistrationPage
import allure


@allure.title("Successful fill form")
def test_success_simple_registration(setup_browser):
    ira = User(
        first_name='Ira',
        last_name='Uchuvatova',
        email='example@mail.ru',
        gender=Gender.female.value,
        phone='1234567890',
        year_of_birth='1986',
        month_of_birth='April',
        day_of_birth='26',
        subjects='Maths',
        hobby='Reading',
        photo='1.png',
        current_address='Sunstreet, 28',
        state='NCR',
        city='Delhi'
    )
    registration_page = ShortRegistrationPage()
    with allure.step("Open registration form"):
        registration_page.open()

    # WHEN
    with allure.step("Fill form"):
        registration_page.register(ira)

    # THEN
    with allure.step("Check results"):
        registration_page.user_should_be_registered(ira)
