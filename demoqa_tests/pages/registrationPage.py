import os

from selene import command
from selene.support.conditions import be, have
from selene.support.shared import browser

import tests
from conftest import setup_browser


class RegistrationPage:
    browser = setup_browser
    def __init__(self):
        self.registered_user_data = browser.element(".table").all("td").even

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.execute_script(
            'document.querySelector(".body-height").style.transform = "scale(.5)"'
        )

    def fill_first_name(self, first_name):
        browser.element("#firstName").should(be.blank).type(first_name)

    def fill_last_name(self, last_name):
        browser.element("#lastName").should(be.blank).type(last_name)

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").should(be.not_.blank).click()
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(".react-datepicker__month-select").send_keys(month).click()
        browser.element(f".react-datepicker__day--0{day}").click()

    def fill_email(self, email):
        browser.element("#userEmail").should(be.blank).type(email)

    def choose_hobbies(self, hobby):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(f'{hobby}')).perform(
            command.js.scroll_into_view).click()

    def choose_gender(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()

    def fill_phone(self, phone):
        browser.element("#userNumber").should(be.blank).type(phone)

    def choose_subjects(self, subject):
        browser.element("#subjectsInput").should(be.blank).type(subject)
        browser.all(".subjects-auto-complete__option").element_by(
            have.exact_text(subject)
        ).click()

    def add_photo(self, path):
        browser.element('input[type="file"]').send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), path)
            )
        )

    def fill_address(self, address, state, city):
        browser.element("#currentAddress").should(be.blank).set_value(address)
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(state)
        ).click()
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(city)
        ).click()

    def submit(self):
        browser.element("#submit").click()

    def should_open_submit_form(self):
        browser.element(".modal-content").element(".modal-header").should(
            have.text("Thanks for submitting the form"))
