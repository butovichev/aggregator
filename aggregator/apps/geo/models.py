from django.db.models import (
    Model,
    CharField,
    SlugField
)
import pytils


class City(Model):
    name = CharField(max_length=100)
    domain_name = CharField(max_length=100)
    slug = SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.slugify(self.name.lower())
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
