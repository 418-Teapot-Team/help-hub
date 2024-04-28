from flask import Blueprint, jsonify
from db.repositories import VolunteerRepository


volunteers_bp = Blueprint("volunteers", __name__, url_prefix="/volunteers")


@volunteers_bp.route("/all", methods=["GET"])
def get_all_volunteers():
    volunteers = VolunteerRepository.get_all()
    return jsonify(volunteers=[item.json() for item in volunteers])
