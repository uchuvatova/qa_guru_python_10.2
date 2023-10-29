from selene import have
from demoqa_tests.pages.registrationPage import RegistrationPage



def test_success_registration():
    registration_page = RegistrationPage()

    registration_page.open()
    # WHEN

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
