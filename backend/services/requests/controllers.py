from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from db.repositories import RequestsRepository
from services.models import UserIdentity, UserRole


requests_bp = Blueprint("request", __name__, url_prefix="/requests")


@requests_bp.route("/create", methods=["POST"])
@jwt_required()
def create_request():

    current_user: UserIdentity = get_jwt_identity()
    if current_user["role"] != UserRole.REQUESTOR.value:
        return jsonify(message="Only requestors can create requests"), 403

    request_data = request.get_json()

    RequestsRepository.create(
        current_user["user_id"],
        request_data["title"],
        request_data["description"],
        request_data["category"],
        request_data["city"],
    )
    return jsonify(message="Request created successfully")


@requests_bp.route("/apply", methods=["POST"])
@jwt_required()
def apply_request():

    current_user: UserIdentity = get_jwt_identity()
    if current_user["role"] != UserRole.VOLUNTEER.value:
        return jsonify(message="You should have a volunteer account to apply."), 403

    data = request.get_json()
    if RequestsRepository.check_if_applied(current_user["user_id"], data["request_id"]):
        return jsonify(message="You have already applied to this request"), 400
    RequestsRepository.apply(data["request_id"], current_user["user_id"])
    return jsonify(message="Successfully applied to request")


@requests_bp.route("/all", methods=["GET"])
def get_all_requests():

    cities = request.args.getlist("cities[]")
    categories = request.args.getlist("categories[]")
    requests = RequestsRepository.get_all(filter_by={"cities": cities, "categories": categories})

    # to show all options
    all_requests = requests
    if cities or categories:
        all_requests = RequestsRepository.get_all()

    request_dict = [
        {
            "id": request.id,
            "title": request.title,
            "description": request.description,
            "category": request.category.name,
            "city": request.city.name,
            "is_active": request.is_active,
            "created_at": request.created_at.strftime("%d/%m/%Y"),
            "requestor": {
                "id": request.requestor.id,
                "full_name": request.requestor.full_name,
                "phone": request.requestor.phone,
                "email": request.requestor.email,
            },
        }
        for request in requests
    ]
    categories = {req.category.id: req.category.name for req in all_requests}
    cities = {req.city.id: req.city.name for req in all_requests}
    filters_dict = {
        "categories": {
            "key": "categories",
            "values": [{"id": key, "name": value} for key, value in categories.items()],
        },
        "cities": {
            "key": "cities",
            "values": [{"id": key, "name": value} for key, value in cities.items()],
        },
    }
    return jsonify(requests=request_dict, filters=filters_dict)


@requests_bp.route("/my", methods=["GET"])
@jwt_required()
def my_requests():

    current_user: UserIdentity = get_jwt_identity()
    if current_user["role"] != UserRole.REQUESTOR.value:
        return jsonify(message="Only requestors can view their requests"), 403

    requests = RequestsRepository.get_by_requestor_id(current_user["user_id"])
    return jsonify(
        [
            {
                "id": request.id,
                "title": request.title,
                "description": request.description,
                "category": request.category.name,
                "city": request.city.name,
                "is_active": request.is_active,
                "created_at": request.created_at.strftime("%d/%m/%Y"),
                "responses": [
                    {
                        "id": response.id,
                        "response": response.response,
                        "volunteer": {
                            "id": response.volunteer.id,
                            "full_name": response.volunteer.full_name,
                            "phone": response.volunteer.phone,
                            "email": response.volunteer.email,
                        },
                        "status": response.status,
                        "created_at": response.created_at.strftime("%d/%m/%Y"),
                    }
                    for response in request.responses
                ],
            }
            for request in requests
        ]
    )
