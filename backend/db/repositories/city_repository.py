from db.models import City
from db import db


class CityRepository:

    @staticmethod
    def get_all():
        return City.query.all()

    @staticmethod
    def create(name: str):
        category = City(name=name)
        db.session.add(category)
        db.session.commit()
        return category
