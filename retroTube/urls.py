from django.urls import path
from . import views

urlpatterns = [
    path('', views.retro_tube, name="retro-tube"),
]