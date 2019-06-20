.. image:: https://dev.azure.com/cameroncairns/django-model-restore/_apis/build/status/CameronCairns.django-model-restore?branchName=master
   :target: https://dev.azure.com/cameroncairns/django-model-restore/_build?definitionId=1
   :alt: CI Status

Django Model Restore: Soft Delete without surprises

This project aims to implement soft delete in Django without some of the
surprises that come with other soft delete libraries. Namely it will
not return soft deleted records from the db when querying on models
related to the model of the soft deleted instance.

Example::

    from django.db import models

    class Owner(soft_delete_lib.Deletable):
        name = models.TextField()
    
    class Poll(soft_delete_lib.Deletable):
        name = models.TextField()
        owner = models.ForeignKey(Owner)
    
    def test_soft_delete():
        owner = Owner.objects.create(name='test')
        poll = Poll.objects.create(name='test', owner=owner)
    
        assert owner.polls.count() == 1
    
        poll.delete()
    
        # works with all soft delete libraries researched
        assert owner.polls.count() == 0
    
        # this is usually where soft delete libraries fail
        assert list(Owner.objects.values_list(poll__name=True, flat=True)) == [None]
    
What's happening here? Most soft delete libraries implement soft delete via a
boolean or date flag (e.g. deleted/deleted_at). They reference this date flag
to determine whether to return the result in the base_queryset for the manager
of the soft deletable model.  What they are not able to do, is have queries
on the same SQL table via other django models respect the filter on the deleted
field. That is the issue this library aims to solve
