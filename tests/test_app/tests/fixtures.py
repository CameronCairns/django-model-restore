from .. import models

import pytest


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass


@pytest.fixture
def main_model():
    return models.MainModel.objects.create(name="main")


@pytest.fixture
def cascade_model(main_model):
    return models.CascadeModel.objects.create(name="cascade", main_model=main_model)


@pytest.fixture
def protect_model(main_model):
    return models.ProtectModel.objects.create(name="protect", main_model=main_model)


@pytest.fixture
def set_null_model(main_model):
    return models.SetNullModel.objects.create(name="set_null", main_model=main_model)


@pytest.fixture
def secondary_model(main_model):
    secondary_model = models.SecondaryModel.objects.create(name="secondary")
    secondary_model.main_models.add(main_model)
    return secondary_model


@pytest.fixture
def tertiary_model(main_model):
    tertiary_model = models.TertiaryModel.objects.create(name="tertiary")
    models.ThroughModel.objects.create(
        main_model=main_model, tertiary_model=tertiary_model) 
    return tertiary_model


@pytest.fixture
def proxy_model(main_model):
    return models.ProxyModel.objects.get(id=main_model.id)


@pytest.fixture
def concrete_model():
    return models.ConcreteModel.objects.create(name="concrete", other_name="concrete2")
