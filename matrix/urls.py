from django.urls import path
from matrix.views import index
urlpatterns = [
    path('', index, name="index"),
]
