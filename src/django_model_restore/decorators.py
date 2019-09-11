"""
Test file for messing with django's meta and archive
"""
from django.db.models import base, fields
from django.db import models

from django.db import transaction

_SOFT_DELETABLE_MODELS = []


class ProxyClassDecoratedError(Exception):
    """
    Error raised when trying to decorate a proxy class with soft delete
    Proxy classes for models that are soft deletable are automatically
    wrapped with soft deletion logic so decoration is unnecessary.
    Furthermore if the concrete model the proxy points to is not
    registered with soft delete, then it is not possible to soft
    delete via the proxy since no archive table has been generated
    for the concrete model
    """


def soft_deletable(cls):
    """
    Registers model with django-model-restore as being soft deletable
    """
    if cls._meta.proxy:
        raise ProxyClassDecoratedError(
            "Proxy classes become soft deletable through the direct or"
            " indirect registration of its concrete model as soft deletable."
        )
    _SOFT_DELETABLE_MODELS.append(cls)
    return cls

def make_soft_deletable():
    """
    Logic to make decorated models archive on deletion

    It would be good to have a concept of deletion groups early on to handle
    restoring deletions via cascade. To simplify you should only restore at
    the level of the model that triggered the cascade.
    """
    pass
