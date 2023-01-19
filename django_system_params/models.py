from uuid import uuid4
from functools import cache

from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class SystemParam(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=80, unique=True)
    value = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name}={self.value}"

    @classmethod
    @cache
    def get(cls, name, default=None):
        try:
            return cls.objects.get(name=name).value
        except cls.DoesNotExist as exception:
            if default is not None:
                return default
            raise exception

    @classmethod
    @cache
    def as_dict(cls):
        return dict(cls.objects.values_list("name", "value"))


@receiver((post_save, post_delete), sender=SystemParam)
def clear_cache(sender, *args, **kwargs):
    sender.get.cache_clear()
    sender.as_dict.cache_clear()
