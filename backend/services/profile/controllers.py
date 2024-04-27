from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.auth.models import repositories


profile_bp = Blueprint("profile", __name__, url_prefix="/profile")


@profile_bp.route("/volunteer/<id>", methods=["GET"])
def volunteer_info(id):
    data = request.get_json()
    if data["role"] not in repositories:
        return jsonify(message="Invalid role"), 400

    repo = repositories[data["role"]]
    user = repo.get_by_id(id)
    if user is None:
        return jsonify(message="No volunteer with such id"), 400
    else:
        return jsonify(
            user_id=user.id,
            full_name=user.full_name,
            phone=user.phone,
            email=user.email,
            closed_requests=user.closed_requests,
            is_verified=user.is_verified,
            description=user.description,
            image_url=user.image_url,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )


@profile_bp.route("/requestor/<id>", methods=["GET"])
def requestor_info(id):
    data = request.get_json()
    if data["role"] not in repositories:
        return jsonify(message="Invalid role"), 400

    repo = repositories[data["role"]]
    user = repo.get_by_id(id)
    if user is None:
        return jsonify(message="No requestor with such id"), 400
    else:
        return jsonify(
            user_id=user.id,
            full_name=user.full_name,
            phone=user.phone,
            email=user.email,
            description=user.description,
            image_url=user.image_url,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )


@profile_bp.route("/edit/<id>", methods=["PUT"])
@jwt_required()
def edit(id):
    # current_user: UserIdentity = get_jwt_identity()
    # repo = repositories[current_user["role"]]
    # user = repo.get_by_id(id)
    return jsonify("To be updated")
