# containers/urls.py

from django.urls import path

from . import views


app_name = "containers"
urlpatterns = [
    # URL pattern for the function-based container list view
    path("fbv", views.container_list_view, name="container-list-fbv"),
    # URL pattern for the class-based container list view
    path("cbv", views.ContainerListView.as_view(), name="container-list-cbv"),
]
