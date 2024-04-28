from db.models import Category
from db import db


class CategoryRepository:

    @staticmethod
    def get_all():
        return Category.query.all()

    @staticmethod
    def create(name: str):
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return category
