### api/models.py ###
from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie
#
# REST - Representational State Transfer -
# a bunch of conventions that define how application should talk to each other over HTTP protocol.
# URL - uniform resource locator, endpoint / webpage / image / video are all resources
#


class MovieResource(ModelResource):     # api endpoint
    class Meta:                         # inner class, define meta-data
        # lazy loading, only load data when needed.
        # In here only return the query, not execute it.
        queryset = Movie.objects.all()
        resource_name = 'movies'        # endpoint URL: api/movies
        excludes = ['date_created']     # remove data fields from http response
