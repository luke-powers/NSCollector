from django.urls import path

from . import views

app_name = 'census_manager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add_census'),
]
