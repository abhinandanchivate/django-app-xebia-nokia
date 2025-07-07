# its my global injector registery.
# all other modules (assets, roles, users) will register their bindings here.==> di.py respective to their module
from injector import Binder
from apps.roles.di import configure_roles_bindings
from apps.users.di import configure_users_bindings
def configure(binder:Binder):
    configure_roles_bindings(binder)
    
    configure_users_bindings(binder)