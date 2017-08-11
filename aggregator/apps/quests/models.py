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
    DecimalField
)


class Schedule(Model):
    url = CharField(max_length=30)


class Contact(Model):
    geo = CharField(max_length=30)
    phone = CharField(max_length=30)
    email = EmailField()
    station = 0
    adress = CharField(max_length=30)
    description = TextField()
    image_map = ImageField(upload_to='img', null=True)


class Quest(Model):
    title = CharField(max_length=30)
    description = TextField()
    schedule = OneToOneField(Schedule)
    contact = OneToOneField(Contact)
    category = ManyToManyField('categories.Category')
    company = OneToOneField('companies.Company')
    partner = ForeignKey('accounts.Partner')
    price = 0


class Image(Model):
    image = ImageField(upload_to='img', null=True)
    quest = ForeignKey(Quest)
    cover = BooleanField(default=False)




