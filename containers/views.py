# containers/views.py

from django.shortcuts import render
from django.views.generic import ListView

from .models import Container


class ContainerListView(ListView):
    """
    Class-based `ListView` for the `contianers.Container` model.
    """

    # We provide the `model` attribute to the `ListView` to specify the model and Django
    # will automatically generate the context variable and template name for us.
    model = Container


def container_list_view(request):
    """
    Function-based list view for the `Container` model.
    """
    # Get all the containers from the database and set them as the variable
    # `container_list`. This variable will be passed to the template through the context
    # dictionary.
    container_list = Container.objects.all()
    return render(
        request,
        # Template which will be used to render the view.
        "containers/container_list.html",
        # Context dictionary which will be passed to the template.
        {"container_list": container_list},
    )
