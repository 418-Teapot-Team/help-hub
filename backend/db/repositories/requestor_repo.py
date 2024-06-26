from db.repositories.base import UserBaseRepository
from db import db
from db.models import Requestor


class RequestorRepository(UserBaseRepository):
    @staticmethod
    def create(full_name: str, phone: str, password: str, email: str):
        phone = RequestorRepository.clear_phone(phone)
        requestor = Requestor(full_name=full_name, phone=phone, password=password, email=email)
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

    @staticmethod
    def update(requestor_id: str, parameters: dict):
        for param in parameters:
            if param == "phone":
                parameters[param] = UserBaseRepository.clear_phone(parameters[param])
            setattr(Requestor.query.get(requestor_id), param, parameters[param])
        db.session.commit()
        return Requestor.query.get(requestor_id)
