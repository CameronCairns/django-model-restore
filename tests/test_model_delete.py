import django_model_restore
import django

import pytest

def test_smoke_test():
    """
    simple test to assert that tox and azure pipelines are working correctly
    """
    assert django_model_restore.__package_name__ == "django-model-restore"
