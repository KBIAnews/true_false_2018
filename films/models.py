from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Film (models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=1024)
    description = models.TextField()
    director = models.CharField(max_length=1024)
    image = models.ImageField(upload_to="images/film_images")
    trailer_embed = models.URLField(max_length=1024, null=True, blank=True)
    convo_author = models.CharField(max_length=1024, null=True, blank=True)
    convo_audio = models.URLField(max_length=1024, null=True, blank=True)
    convo_text = models.TextField(null=True, blank=True)
    convo_with = models.CharField(max_length=1024, null=True, blank=True)

    class Meta:
        ordering = ['slug']

    def get_absolute_url(self):
        return "/films/%s/" % self.slug

    def __str__(self):
        return "%s" % self.title

class Venue (models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=1024)
    address = models.TextField()
    description = models.TextField()
    lat = models.FloatField()
    long = models.FloatField()

    def get_absolute_url(self):
        return "/venues/%s/" % self.slug

    def __str__(self):
        return "%s" % self.name

class Screening (models.Model):
    film = models.ForeignKey(Film)
    venue = models.ForeignKey(Venue)
    screening_time = models.DateTimeField()

    class Meta:
        ordering = ['screening_time']

    def __str__(self):
        return "%s %s" % (self.film.title, self.screening_time.strftime('%Y-%m-%d %H:%M'))