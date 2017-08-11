from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    TextField,
    DateTimeField,
    ImageField,
    ManyToManyField,
    BooleanField,
    OneToOneField,
    EmailField,
)
from django.contrib.auth.models import User
from django.db import models


class Gamer(Model):
    phone = models.CharField(max_length=30, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="gamer")
    photo = ImageField(upload_to='img', null=True)

    # def user_post_save(sender, instance, **kwargs):
    #     profile, new = Gamer.objects.get_or_create(user=instance)

    # models.signals.post_save.connect(user_post_save, sender=User)


class Partner(Model):
    name = CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="partner")

    def user_post_save(sender, instance, **kwargs):
        profile, new = Partner.objects.get_or_create(user=instance)

    models.signals.post_save.connect(user_post_save, sender=User)
