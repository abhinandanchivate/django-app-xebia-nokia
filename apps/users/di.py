# DI for users
from injector import Binder, singleton
from apps.users.service import UserService
from apps.users.repository import UserRepository
def configure_users_bindings(binder: Binder):
    """
    Configure the bindings for the users module.
    This function is used to register the UserService and UserRepository
    with the injector.
    """
    binder.bind(UserService, to=UserService, scope=singleton)
    binder.bind(UserRepository, to=UserRepository, scope=singleton)