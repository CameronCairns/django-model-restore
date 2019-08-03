"""
Collection of models in order to test django-model-restore

Need to test deletion behavior given the variety of model
types and model relationships that Django supports
"""
from django.db import models


class AbstractModel(models.Model):

    class Meta:
        abstract = True


class MainModel(AbstractModel):
    name = models.TextField()


class CascadeModel(models.Model):
    name = models.TextField()
    main_model = models.ForeignKey(MainModel, on_delete=models.CASCADE)


class ProtectModel(models.Model):
    name = models.TextField()
    main_model = models.ForeignKey(MainModel, on_delete=models.PROTECT)


class SetNullModel(models.Model):
    name = models.TextField()
    main_model = models.ForeignKey(MainModel, null=True, on_delete=models.SET_NULL)


class SecondaryModel(models.Model):
    name = models.TextField()
    main_models = models.ManyToManyField(MainModel)


class TertiaryModel(models.Model):
    name = models.TextField()
    main_models = models.ManyToManyField(MainModel, through="ThroughModel")


class ThroughModel(models.Model):
    main_model = models.ForeignKey(MainModel, on_delete=models.CASCADE)
    tertiary_model = models.ForeignKey(TertiaryModel, on_delete=models.CASCADE)


class ProxyModel(MainModel):

    class Meta:
        proxy = True


class ConcreteModel(MainModel):
    other_name = models.TextField()
