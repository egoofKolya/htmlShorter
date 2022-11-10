from django.db import models


# Create your models here.
class Urls(models.Model):
    short_id = models.SlugField(max_length=6, primary_key=True)
    httpurl = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    days = models.IntegerField(default=90)
