from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^(?P<short_id>\w{6})$', views.redirect_original, name='redirect_original'),
    path('shorten_url/', views.shorten_url, name='shorten_url'),
]

# urlpatterns = [
#     re_path(r'^$', 'home', name='home'),
#     # for our home/index page
#
#     re_path(r'^(?P<short_id>\w{6})$', 'redirect_original', name='redirectoriginal'),
#     # when short URL is requested it redirects to original URL
#
#     re_path(r'^makeshort/$', 'shorten_url', name='shortenurl'),
#     # this will create a URL's short id and return the short URL
# )
# ]
