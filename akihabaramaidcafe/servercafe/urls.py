from . import views
from django.urls import path

urlpatterns = [
    path("customerin", views.customerin, name="cutomerin")
]