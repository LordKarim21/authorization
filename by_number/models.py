from django.db import models


class Profile(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    invite_code = models.CharField(max_length=6, null=True, blank=True)
    code = models.CharField(max_length=4, blank=True, null=True)
    activated_invite_code = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number
