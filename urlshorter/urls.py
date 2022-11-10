from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('short_id/', views.short_id, name='short_id'),
    path('urlshorter/', views.urlshorter, name='urlshorter'),
]
