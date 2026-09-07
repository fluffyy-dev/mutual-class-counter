from django.urls import path
from . import views
from .views import get_moots_view

urlpatterns = [
    path("", views.home, name="home"),
    path("mutuals/", views.mutuals, name="mutuals"),
    path("get-moots/", get_moots_view, name="get_moots"),
]