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


class Category(Model):
    title = CharField(max_length=30)
    image = ImageField(upload_to='img', null=True)

