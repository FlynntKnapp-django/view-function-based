from django.shortcuts import render
from django.views.generic import ListView

from .models import Container


# Class-based view
class ContainerListView(ListView):
    model = Container


# Function-based view
def container_list_view(request):
    container_list = Container.objects.all()
    return render(
        request, "containers/container_list.html", {"container_list": container_list}
    )
