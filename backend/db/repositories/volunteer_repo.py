from db.repositories.base import UserBaseRepository
from db import db
from db.models import Volunteer


class VolunteerRepository(UserBaseRepository):

    @staticmethod
    def create(full_name: str, phone: str, password: str):
        phone = VolunteerRepository.clear_phone(phone)
        volunteer = Volunteer(full_name=full_name, phone=phone, password=password)
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
