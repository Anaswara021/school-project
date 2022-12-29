from django.urls import path
from .views import index,home,logi,log,menuu,registr


urlpatterns=[
    path('index/',index),
    path('home/',home),
    path('logi/',logi),
    path('log/',log),
    path('menu/',menuu),
    path('registr/',registr)

]