"""
Basic tests around the setup of the app being successful

Want to assert starting assumptions of state of fixtures
"""
import pytest


from .. import models

from .fixtures import (
    main_model,
    cascade_model,
    protect_model,
    set_null_model,
    secondary_model,
    tertiary_model,
    proxy_model,
    concrete_model,
)

def test_main_model(main_model):
    assert main_model.name == "main"
    assert models.MainModel.objects.count() == 1


def test_cascade_model(main_model, cascade_model):
    assert cascade_model.name == "cascade"
    assert cascade_model.main_model == main_model
    assert models.CascadeModel.objects.count() == 1


def test_protect_model(main_model, protect_model):
    assert protect_model.name == "protect"
    assert protect_model.main_model == main_model
    assert models.ProtectModel.objects.count() == 1


def test_set_null_model(main_model, set_null_model):
    assert set_null_model.name == "set_null"
    assert set_null_model.main_model == main_model
    assert models.SetNullModel.objects.count() == 1


def test_secondary_model(main_model, secondary_model):
    assert secondary_model.name == "secondary"
    assert set(secondary_model.main_models.all()) == set([main_model])
    assert models.SecondaryModel.objects.count() == 1


def test_tertiary_model(main_model, tertiary_model):
    assert tertiary_model.name == "tertiary"
    assert set(tertiary_model.main_models.all()) == set([main_model])
    assert models.TertiaryModel.objects.count() == 1
    assert models.ThroughModel.objects.count() == 1
    through_model = models.ThroughModel.objects.get()
    assert through_model.main_model == main_model
    assert through_model.tertiary_model == tertiary_model


def test_proxy_model(proxy_model):
    assert proxy_model.name == "main"


def test_concrete_model(concrete_model):
    assert concrete_model.name == "concrete"
    assert concrete_model.other_name == "concrete2"
    assert models.ConcreteModel.objects.count() == 1
    assert models.MainModel.objects.count() == 1
    assert models.MainModel.objects.get() == concrete_model.mainmodel_ptr
