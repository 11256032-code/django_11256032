from django.urls import path
from . import views

urlpatterns = [
    path('whoaml/', views.whoaml, name='whoaml'),
]
