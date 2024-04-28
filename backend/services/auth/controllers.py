import datetime
from typing import Union
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

from db.models import Requestor, Volunteer
from services.models import repositories, UserIdentity


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    if data["role"] not in repositories:
        return jsonify(message="Invalid role"), 400

    repo = repositories[data["role"]]
    user = repo.get_by_phone(data["phone"])
    if user:
        return jsonify(message="User already exists"), 400
    else:
        new_user = repo.create(
            full_name=data["full_name"],
            phone=data["phone"],
            password=generate_password_hash(data["password"]),
            email=data["email"],
        )
        access_token = create_access_token(
            identity=UserIdentity(user_id=new_user.id, role=data["role"]), expires_delta=datetime.timedelta(days=1)
        )
        return jsonify(message="Successfully signed up!", access_token=access_token)


@auth_bp.route("/signin", methods=["POST"])
def signin():
    data = request.get_json()
    if data["role"] not in repositories:
        return jsonify(message="Invalid role"), 400
    repo = repositories[data["role"]]
    user = repo.get_by_phone(data["phone"])
    if user and check_password_hash(user.password, data["password"]):
        access_token = create_access_token(
            identity=UserIdentity(user_id=user.id, role=data["role"]), expires_delta=datetime.timedelta(days=1)
        )
        return jsonify(access_token=access_token, message="Successfully signed in!")
    else:
        return jsonify(message="Invalid phone or password"), 401


@auth_bp.route("/whoami", methods=["GET"])
@jwt_required()
def whoami():
    current_user: UserIdentity = get_jwt_identity()
    repo = repositories[current_user["role"]]
    user: Union[Volunteer, Requestor] = repo.get_by_id(current_user["user_id"])

    return jsonify(user.json())
