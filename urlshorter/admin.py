from django.contrib import admin
from .models import Urls
# Register your models here.


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'httpurl', 'pub_date', 'days')
    ordering = ('-pub_date',)


admin.site.register(Urls, UrlsAdmin)
