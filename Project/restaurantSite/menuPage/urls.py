from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('person_data', views.person_data_view, name="person_data"),
    path('success', views.success, name='success'),
]