# Import all the models, so that Base has them before being
# imported by Alembic
from .base_class import Base  # noqa isort:skip

# from .models.identityaccess import Loja, RolePermissions, Roles, Tenant, User  # noqa

__all__ = ["Base"]
