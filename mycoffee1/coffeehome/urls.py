from django.contrib import admin
from django.urls import path
from coffeehome.views import *

urlpatterns = [
    path('index/',index),

    path('about/', about),

    path('blog/', blog),

    path('locations/', locations),

    path('menu/', menu),


]