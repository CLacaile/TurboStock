from app.models import *


def has_permission_on_item(user, item):
    user = user.child_object()
    user_class = type(user).__name__
    item_class = type(item).__name__

    # If user isCEO
    if user_class == CEO.__name__:
        return True

    # If user is StoreManager
    if user_class == StoreManager.__name__:
        # If item is Store
        if item_class == Store.__name__:
            if item.id == user.store_id:
                return True
        # If item is Aisle
        if item_class == Aisle.__name__:
            if item.store_id == user.store_id:
                return True
        return False

    # If user is AisleManager
    if user_class == AisleManager.__name__:
        # If item is Store
        if item_class == Store.__name__:
            return False
        # If item is Aisle
        if item_class == Aisle.__name__:
            if item.id == user.aisle_id:
                return True
        return False
