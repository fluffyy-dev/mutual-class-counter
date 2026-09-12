from django.urls import path
from . import views
from .views import get_moots_view

urlpatterns = [
    path("", views.home, name="home"),
    path("mutuals/", views.mutuals, name="mutuals"),
    path("frame-maker/", views.frame_maker, name="frame-maker"),
    path("flowers/", views.flowers, name="flowers"),
    path("to-do/", views.to_do, name="to-do"),

    path("get-moots/", get_moots_view, name="get_moots"),
]