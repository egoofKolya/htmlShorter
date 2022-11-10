import random, string, json
from django.shortcuts import render, get_object_or_404
from .models import Urls
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.context_processors import csrf
# Create your views here.

def home():
    c = {}
