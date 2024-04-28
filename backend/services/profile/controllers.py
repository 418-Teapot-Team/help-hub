from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth.models import repositories
from .models import UserIdentity

profile_bp = Blueprint("profile", __name__, url_prefix="/profile")


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


@profile_bp.route("/edit/<id>", methods=["PUT"])
@jwt_required()
def edit(id):
    current_user: UserIdentity = get_jwt_identity()
    repo = repositories[current_user["role"]]
    data = dict(request.get_json())
    updated_user = repo.update(id, data)
    if current_user["role"] == "requestor":
        return jsonify(
            user_id=updated_user.id,
            full_name=updated_user.full_name,
            phone=updated_user.phone,
            email=updated_user.email,
            description=updated_user.description,
            image_url=updated_user.image_url,
            created_at=updated_user.created_at,
            updated_at=updated_user.updated_at,
        )
    elif current_user["role"] == "volunteer":
        return jsonify(
            user_id=updated_user.id,
            full_name=updated_user.full_name,
            phone=updated_user.phone,
            email=updated_user.email,
            closed_requests=updated_user.closed_requests,
            is_verified=updated_user.is_verified,
            description=updated_user.description,
            image_url=updated_user.image_url,
            created_at=updated_user.created_at,
            updated_at=updated_user.updated_at,
        )
    else:
        return jsonify(message="Error at updating"), 400
