from models import UserRole, User

USERS = (
    User(id=1, name='Andy', role=UserRole.admin.value),
    User(id=2, name='Nik', role=UserRole.user.value),
    User(id=3, name='Alex', role=UserRole.manager.value),
    User(id=4, name='Beck', role=UserRole.user.value),
    User(id=5, name='Lance', role=UserRole.admin.value),
)
