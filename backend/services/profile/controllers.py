from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.models import repositories, UserIdentity

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")


@profile_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    current_user: UserIdentity = get_jwt_identity()
    repo = repositories[current_user["role"]]
    user = repo.get_by_id(current_user["user_id"])

    if not user:
        return jsonify(message="Error at getting user"), 400

    return jsonify(user.json())


@profile_bp.route("/edit", methods=["PUT"])
@jwt_required()
def edit():
    current_user: UserIdentity = get_jwt_identity()
    repo = repositories[current_user["role"]]
    data = dict(request.get_json())
    updated_user = repo.update(current_user["user_id"], data)
    if updated_user:
        return jsonify(message="Successfully updated"), 200
    else:
        return jsonify(message="Error at updating"), 400


@profile_bp.route("/volunteer/<id>", methods=["GET"])
def volunteer_info(id):
    repo = repositories["volunteer"]
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
    repo = repositories["requestor"]
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
