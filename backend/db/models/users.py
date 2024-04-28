from db.models.base import db


class Volunteer(db.Model):
    __tablename__ = "volunteers"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    closed_requests = db.Column(db.Integer, nullable=False, default=0)
    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    telegram = db.Column(db.String(50), nullable=True)
    instagram = db.Column(db.String(50), nullable=True)
    facebook = db.Column(db.String(50), nullable=True)
    twitter = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Volunteer {self.first_name} {self.last_name}>"

    def json(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "phone": self.phone,
            "email": self.email,
            "closed_requests": self.closed_requests,
            "is_verified": self.is_verified,
            "description": self.description,
            "image_url": self.image_url,
            "created_at": self.created_at.strftime("%d/%m/%Y"),
            "updated_at": self.updated_at.strftime("%d/%m/%Y"),
            "telegram": self.telegram,
            "instagram": self.instagram,
            "facebook": self.facebook,
            "twitter": self.twitter,
            "role": "volunteer",
        }


class Requestor(db.Model):
    __tablename__ = "requestors"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    telegram = db.Column(db.String(50), nullable=True)
    instagram = db.Column(db.String(50), nullable=True)
    facebook = db.Column(db.String(50), nullable=True)
    twitter = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<Requestor {self.first_name} {self.last_name}>"

    def json(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "phone": self.phone,
            "email": self.email,
            "description": self.description,
            "image_url": self.image_url,
            "created_at": self.created_at.strftime("%d/%m/%Y"),
            "updated_at": self.updated_at.strftime("%d/%m/%Y"),
            "telegram": self.telegram,
            "instagram": self.instagram,
            "facebook": self.facebook,
            "twitter": self.twitter,
            "role": "requestor",
        }
