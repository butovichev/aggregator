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
    SlugField
)

from django.utils import timezone
import pytils

from ckeditor.fields import RichTextField


class Article(Model):
    STATUS_CHOICES = (
        ('draft', 'draft'),
        ('public', 'public'),
        ('delete', 'delete')
    )

    author = ForeignKey('auth.User')

    title = CharField(max_length=200)

    slug = SlugField(blank=True, editable=False)

    description = TextField(blank=True)

    text = RichTextField()

    created_at = DateField(default=timezone.now)

    public_at = DateField(blank=True, null=True)

    status = CharField(choices=STATUS_CHOICES, default='draft', max_length=10)

    city = ForeignKey('geo.City', null=True)

    media = ImageField(upload_to='media/%Y/%m/%d',
                       null=True,
                       blank=True,
                       help_text="Upload your photo for post")

    def update(self):
        if self.status == 'public':
            self.public_at = timezone.now
            self.save()

    def save(self, *args, **kwargs):
        self.slug = pytils.translit.slugify(self.title.lower())
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Detail Article'
        verbose_name_plural = 'Article'
        # ordering = ["-public_date"]
