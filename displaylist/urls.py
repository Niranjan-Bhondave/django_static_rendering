from django.urls import path
from . import views

urlpatterns = [
    path("", views.displayList, name='displayList'),
]