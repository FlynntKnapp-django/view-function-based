# containers/urls.py

from django.urls import path

from . import views


app_name = "containers"
urlpatterns = [
    path("fbv", views.container_list_view, name="container-list-fbv"),
    path("cbv", views.ContainerListView.as_view(), name="container-list-cbv"),
]
