from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name="about"),#/about이라고 할떄
    path('result/', wordcount.views.result, name="result"),
]
