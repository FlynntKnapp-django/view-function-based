from django.urls import path

from .views import container_list_view, ContainerListView


app_name = "containers"
urlpatterns = [
    path("fbv", container_list_view, name="container-list-fbv"),
    path("cbv", ContainerListView.as_view(), name="container-list-cbv"),
]
