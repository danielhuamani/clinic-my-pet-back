from django.db import models
from django.utils.translation import gettext as _


class Pet(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_pets")
    name = models.CharField("name", max_length=255)
    weight = models.DecimalField("weight", decimal_places=2)
    gender = models.CharField("gender", max_length=255)
    birthday = models.DateTimeField("birthday")
    colour = models.CharField("colour", max_length=255)

    class Meta:
        verbose_name = _("Pet")
        verbose_name_plural = _("Pets")

    def __str__(self):
        return self.name
