from typing import TypedDict
import services.models
from db.repositories import VolunteerRepository, RequestorRepository, UserBaseRepository


repositories: dict[services.models.UserRole, UserBaseRepository] = {
    services.models.UserRole.VOLUNTEER.value: VolunteerRepository,
    services.models.UserRole.REQUESTOR.value: RequestorRepository,
}


class UserIdentity(TypedDict):
    user_id: str
    role: services.models.UserRole
