from injector import Binder, Injector, singleton
from apps.roles.service import RoleService
from apps.roles.repository import RoleRepository

def configure_roles_bindings(binder: Binder) :
    """
    Configure the bindings for the roles module.
    This function is used to register the RoleService and RoleRepository
    with the injector.
    """
    binder.bind(RoleService, to=RoleService, scope=singleton)
    binder.bind(RoleRepository, to=RoleRepository, scope=singleton)