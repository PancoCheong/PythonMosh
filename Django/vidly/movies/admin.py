# movies/admin.py
from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# the data attributes that we can override
class MovieAdmin(admin.ModelAdmin):
    # fields = ('title', 'genre')         # defines the fields shown on the form
    # single value in tuple, need to add , if not, Python treat it as string with ()
    exclude = ('date_created',)         # fields that we don't want to show
    list_display = ('title', 'number_in_stock', 'daily_rate')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
