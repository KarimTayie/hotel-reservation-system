from django.db import models
from django.utils.translation import gettext_lazy as _


class RoomType(models.TextChoices):
    SINGLE = "single", _("Single")
    DOUBLE = "double", _("Double")
    SUITE = "suite", _("Suite")
