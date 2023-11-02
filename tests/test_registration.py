import allure
from allure_commons.types import Severity
from selene import have

#from conftest import setup_browser
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
    with allure.step("Fill first name"):
        registration_page.fill_first_name('Ira')
    with allure.step("Fill last name"):
        registration_page.fill_last_name('Uchuvatova')
    with allure.step("Choose hobby"):
        registration_page.choose_hobbies('Reading')
    with allure.step("Fill date of birth"):
        registration_page.fill_date_of_birth('1986', 'April', 26)
    with allure.step("Fill email"):
        registration_page.fill_email('example@mail.ru')
    with allure.step("Choose gender"):
        registration_page.choose_gender('Female')
    with allure.step("Fill phone"):
        registration_page.fill_phone('1234567890')
    with allure.step("Choose subjects"):
        registration_page.choose_subjects('Maths')
    with allure.step("Add photo"):
        registration_page.add_photo('resourses/1.png')
    with allure.step("Fill address"):
        registration_page.fill_address('Sunstreet, 28', 'NCR', 'Delhi')
    with allure.step("Submit form"):
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
