from db.models import Request, Category, RequestResponses, City
from db import db


class RequestsRepository:

    @staticmethod
    def create(requestor_id: str, title: str, description: str, category: str, city: str):
        category = Category.query.filter_by(name=category).first()
        city = City.query.filter_by(name=city).first()
        request = Request(
            requestor_id=requestor_id, title=title, description=description, category_id=category.id, city_id=city.id
        )
        db.session.add(request)
        db.session.commit()
        return request

    @staticmethod
    def get_all(filter_by=None, search=None, get_inactive=False):
        query = Request.query
        # filter by cities passed as list
        if filter_by and filter_by.get("cities"):
            query = query.filter(Request.city_id.in_(filter_by["cities"]))
        if filter_by and filter_by.get("categories"):
            query = query.filter(Request.category_id.in_(filter_by["categories"]))
        if not get_inactive:
            query = query.filter_by(is_active=True)
        return query.all()

    @staticmethod
    def apply(volunteer_id: str, request_id: str):
        request_response = RequestResponses(volunteer_id=volunteer_id, request_id=request_id)
        db.session.add(request_response)
        db.session.commit()

    @staticmethod
    def check_if_applied(volunteer_id: str, request_id: str):
        return RequestResponses.query.filter_by(volunteer_id=volunteer_id, request_id=request_id).first()

    @staticmethod
    def get_by_requestor_id(requestor_id: str):
        return Request.query.filter_by(requestor_id=requestor_id, is_active=True).all()

    @staticmethod
    def get_appliers(request_id: str):
        print("request_id", request_id)
        return RequestResponses.query.filter_by(request_id=request_id, status="PENDING").all()
