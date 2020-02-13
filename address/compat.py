from django.db.models.fields.related import ForeignObject


def compat_contribute_to_class(self, cls, name, virtual_only=False):
    super(ForeignObject, self).contribute_to_class(cls, name)
