from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Band(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.genre}')
        super(Band, self).save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('about', kwargs={"slug": self.slug})
