from demoqa_tests.data.users import User, Gender
from demoqa_tests.pages.shortRegistrationPage import ShortRegistrationPage


def test_success_simple_registration():
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
    registration_page.open()

    # WHEN
    registration_page.open()
    registration_page.register(ira)

    # THEN
    registration_page.user_should_be_registered(ira)
