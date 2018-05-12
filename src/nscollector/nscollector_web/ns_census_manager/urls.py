from django.urls import include, path

from . import views, resources

census_resource = resources.CensusResource()

app_name = 'census_manager'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add_census'),
    path('api/', include(census_resource.urls)),
]
