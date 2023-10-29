import os
from pathlib import Path

from selene import command
from selene.support.conditions import be, have
from selene.support.shared import browser


class ShortRegistrationPage:
    def __init__(self):
        self.registered_user_data = browser.element(".table").all("td").even

    def open(self):
        browser.open("/automation-practice-form")
        browser.execute_script(
            'document.querySelector(".body-height").style.transform = "scale(.5)"'
        )

    def register(self, user):
        browser.element("#firstName").should(be.blank).type(user.first_name)
        browser.element("#lastName").should(be.blank).type(user.last_name)
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(f'{user.hobby}')).perform(
            command.js.scroll_into_view).click()
        browser.element("#dateOfBirthInput").should(be.not_.blank).click()
        browser.element(".react-datepicker__year-select").type(user.year_of_birth)
        browser.element(".react-datepicker__month-select").send_keys(user.month_of_birth).click()
        browser.element(f".react-datepicker__day--0{user.day_of_birth}").click()
        browser.element("#userEmail").should(be.blank).type(user.email)
        browser.element(f'[name=gender][value={user.gender}]+label').click()
        browser.element("#userNumber").should(be.blank).type(user.phone)
        browser.element("#subjectsInput").should(be.blank).type(user.subjects)
        browser.all(".subjects-auto-complete__option").element_by(
            have.exact_text(user.subjects)
        ).click()
        browser.element("#uploadPicture").send_keys(os.path.abspath(
            Path(__file__).parent.parent.parent.joinpath(f'tests/resourses/{user.photo}')))
        browser.element("#currentAddress").should(be.blank).set_value(user.current_address)
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(user.state)
        ).click()
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(user.city)
        ).click()
        browser.element("#submit").click()

    def user_should_be_registered(self, user):
        browser.element(".modal-content").element(".modal-header").should(
            have.text("Thanks for submitting the form"))
        user.date_of_birth = f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}'
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone,
                user.date_of_birth,
                user.subjects,
                user.hobby,
                user.photo,
                user.current_address,
                f'{user.state} {user.city}',
            )
        )
