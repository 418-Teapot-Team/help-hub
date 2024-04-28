from flask import Blueprint, jsonify

from services.models import repositories

stat_bp = Blueprint("stat", __name__, url_prefix="/stat")


@stat_bp.route("/general", methods=["GET"])
def general():
    repo = repositories["volunteer"]
    amount_volunteers = len(repo.get_all())

    repo = repositories["requests"]
    amount_requests = len(repo.get_all())
    amount_done_requests = len([request for request in repo.get_all() if request.is_active is False])

    return (
        jsonify(
            {
                "amount_volunteers": amount_volunteers,
                "amount_requests": amount_requests,
                "amount_done_requests": amount_done_requests,
            }
        ),
        200,
    )
