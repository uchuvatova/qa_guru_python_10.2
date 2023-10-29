import dataclasses
import enum


class Gender(enum.Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subjects: str
    hobby: str
    photo: str
    current_address: str
    state: str
    city: str
