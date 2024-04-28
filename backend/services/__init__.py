from .controllers import api_bp
from .auth.controllers import auth_bp
from .profile.controllers import profile_bp
from .requests.controllers import requests_bp

api_bp.register_blueprint(auth_bp)
api_bp.register_blueprint(profile_bp)
api_bp.register_blueprint(requests_bp)
