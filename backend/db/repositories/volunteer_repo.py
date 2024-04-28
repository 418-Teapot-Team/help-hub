from db.repositories.base import UserBaseRepository
from db import db
from db.models import Volunteer


class VolunteerRepository(UserBaseRepository):

    @staticmethod
    def create(full_name: str, phone: str, password: str, email: str):
        phone = VolunteerRepository.clear_phone(phone)
        volunteer = Volunteer(full_name=full_name, phone=phone, password=password, email=email)
        db.session.add(volunteer)
        db.session.commit()
        return volunteer

    @staticmethod
    def get_by_id(volunteer_id: str):
        return Volunteer.query.get(volunteer_id)

    @staticmethod
    def get_by_phone(phone: str):
        phone = VolunteerRepository.clear_phone(phone)
        return Volunteer.query.filter_by(phone=phone).first()

    @staticmethod
    def update(volunteer_id: str, parameters: dict):
        for param in parameters:
            if param == "phone":
                parameters[param] = UserBaseRepository.clear_phone(parameters[param])
            setattr(Volunteer.query.get(volunteer_id), param, parameters[param])
        db.session.commit()
        return Volunteer.query.get(volunteer_id)
