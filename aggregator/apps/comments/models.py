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

from aggregator.apps.quests.models import Quest
from aggregator.apps.accounts.models import Gamer
# from aggregator.apps.user.models import User


class Rating(Model):
    field = CharField(max_length=30)


class Comment(Model):
    date = DateField()
    gamer = ForeignKey(Gamer)
    text = TextField()
    rating = ForeignKey(Rating)
    quest = ForeignKey(Quest)



