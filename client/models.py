import enum
from dataclasses import dataclass


class UserRole(enum.Enum):
    admin: str = 'ADMIN'
    manager: str = 'MANAGER'
    user: str = 'USER'


@dataclass
class User:
    id: int
    name: str
    role: UserRole = UserRole.user
