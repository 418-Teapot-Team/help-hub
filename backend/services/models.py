from typing import TypedDict
from db.repositories import VolunteerRepository, RequestorRepository, UserBaseRepository
from enum import Enum


class UserRole(Enum):
    VOLUNTEER = "volunteer"
    REQUESTOR = "requestor"


repositories: dict[UserRole, UserBaseRepository] = {
    UserRole.VOLUNTEER.value: VolunteerRepository,
    UserRole.REQUESTOR.value: RequestorRepository,
}


class UserIdentity(TypedDict):
    user_id: str
    role: UserRole
