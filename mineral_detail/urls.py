from django.urls import path

from . import views

urlpatterns = [
    path('<int:mineral_id>/', views.mineral_detail, name='mineral_detail'),
]
