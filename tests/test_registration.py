import allure
from allure_commons.types import Severity
from selene import have

from conftest import setup_browser
from demoqa_tests.pages.registrationPage import RegistrationPage


@allure.title("Successful fill form")
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "irauchuvatova")
@allure.feature("Задачи в репозитории")
@allure.story("Пользователь заполняет регистрационную форму")
@allure.link("https://demoqa.com/automation-practice-form", name="Ссылка на форму регистрации")
def test_success_registration(setup_browser):
    registration_page = RegistrationPage()
    with allure.step("Open registration form"):
        registration_page.open()
    # WHEN
    with allure.step("Fill form"):
        registration_page.fill_first_name('Ira')
        registration_page.fill_last_name('Uchuvatova')
        registration_page.choose_hobbies('Reading')
        registration_page.fill_date_of_birth('1986', 'April', 26)
        registration_page.fill_email('example@mail.ru')
        registration_page.choose_gender('Female')
        registration_page.fill_phone('1234567890')
        registration_page.choose_subjects('Maths')
        registration_page.add_photo('resourses/1.png')
        registration_page.fill_address('Sunstreet, 28', 'NCR', 'Delhi')
        registration_page.submit()

    # THEN
    with allure.step("Check results"):
        registration_page.should_open_submit_form()
        registration_page.registered_user_data.should(
            have.exact_texts(
                "Ira Uchuvatova",
                "example@mail.ru",
                "Female",
                "1234567890",
                "26 April,1986",
                "Maths",
                "Reading",
                "1.png",
                "Sunstreet, 28",
                "NCR Delhi"))
