from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    """
    class for gender api model
    """
    MALE = "male"
    FEMALE = "female"


class Role(str, Enum):
    """
    class for roles in api model
    """
    ADMIN = "admin"
    USER = "user"


class User(BaseModel):
    """
    class for user fields in api
    """
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]


class ChangeUser(BaseModel):
    """
    class to update user fields in api
    """
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]
