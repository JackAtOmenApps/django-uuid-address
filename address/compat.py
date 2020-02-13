import django
from django.db.models.fields.related import ForeignObject

django_version = django.VERSION


def compat_contribute_to_class(self, cls, name, virtual_only=False):
    super(ForeignObject, self).contribute_to_class(
        cls, name, virtual_only=virtual_only)
