from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    TextField,
    DateField,
    ImageField,
    ManyToManyField,
    BooleanField,
    OneToOneField,
    EmailField,
)


class Company(Model):
    name = CharField(max_length=30)

