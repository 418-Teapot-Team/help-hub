from db.repositories.base import UserBaseRepository
from db import db
from db.models import Requestor


class RequestorRepository(UserBaseRepository):

    @staticmethod
    def create(full_name: str, phone: str, password: str):
        phone = RequestorRepository.clear_phone(phone)
        requestor = Requestor(full_name=full_name, phone=phone, password=password)
        db.session.add(requestor)
        db.session.commit()
        return requestor

    @staticmethod
    def get_by_id(requestor_id: str):
        return Requestor.query.get(requestor_id)

    @staticmethod
    def get_by_phone(phone: str):
        phone = RequestorRepository.clear_phone(phone)
        return Requestor.query.filter_by(phone=phone).first()
