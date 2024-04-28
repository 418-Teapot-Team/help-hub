from flask import Blueprint, jsonify
from db.repositories import CategoryRepository, CityRepository


api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/categories", methods=["GET"])
def get_categories():
    categories = CategoryRepository.get_all()
    return jsonify([{"id": category.id, "name": category.name} for category in categories])


@api_bp.route("/cities", methods=["GET"])
def get_cities():
    cities = CityRepository.get_all()
    return jsonify([{"id": city.id, "name": city.name} for city in cities])
