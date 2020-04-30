# movies/models.py
from django.db import models
from django.utils import timezone

# Django Model handles how to save data in database


class Genre(models.Model):
    name = models.CharField(max_length=255)
    # models.BooleanField, models.IntegerField, models.FloatField

    # default output:"Gener object(1)"
    # override it to print its content
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # define relationship with other model
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # add new field
    #
    # problem: datetime object is not aware of time zone.
    # from datetime import datetime
    # date_created = models.DateTimeField(default=datetime.now
    #
    # better to use timezone object in django
    # it can auto translate the datetime to user's timezone
    # from django.utils import timezone
    #
    # pass reference to method, no ()
    # if use timezone.now(), the value is fixed date value of this moment in time.
    date_created = models.DateTimeField(default=timezone.now)
