from db.models import Request, Category, RequestResponses
from db import db


class RequestsRepository:

    @staticmethod
    def create(requestor_id: str, title: str, description: str, category: str):
        category = Category.query.filter_by(name=category).first()
        request = Request(requestor_id=requestor_id, title=title, description=description, category_id=category.id)
        db.session.add(request)
        db.session.commit()
        return request

    @staticmethod
    def get_all():
        return Request.query.all()

    @staticmethod
    def apply(volunteer_id: str, request_id: str):
        request_response = RequestResponses(volunteer_id=volunteer_id, request_id=request_id)
        db.session.add(request_response)
        db.session.commit()

    @staticmethod
    def get_by_requestor_id(requestor_id: str):
        return Request.query.filter_by(requestor_id=requestor_id).all()

    @staticmethod
    def get_appliers(request_id: str):
        return RequestResponses.query.filter_by(request_id=request_id, status="PENDING").all()
