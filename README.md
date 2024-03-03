# Django Function-Based View Example

Example for function-based Django view.

## Directory Structure

```bash
PS C:\Users\FlynntKnapp\Programming\view-function-based> tree /a /f
Folder PATH listing
Volume serial number is 40CB-1E6B
C:.
|   .gitignore
|   db.sqlite3
|   LICENSE
|   manage.py
|   Pipfile
|   Pipfile.lock
|   README.md
|
+---config
|       asgi.py
|       settings.py
|       urls.py
|       wsgi.py
|       __init__.py
|
\---containers
    |   admin.py
    |   apps.py
    |   models.py
    |   tests.py
    |   urls.py
    |   views.py
    |   __init__.py
    |
    +---migrations
    |       0001_initial.py
    |       __init__.py
    |
    \---templates
        \---containers
                container_list.html

PS C:\Users\FlynntKnapp\Programming\view-function-based>
```

## Important Project Files

### `config/settings.py`

```python
# config/settings.py

INSTALLED_APPS = [
    # ...
    "containers.apps.ContainersConfig",
    # ...
]
```

### `config/urls.py`

```python
# config/urls.py

# ...
from django.urls import include, path

urlpatterns = [
    # ...
    path("containers/", include("containers.urls")),
    # ...
]
```

## Important Application Files

### `containers/apps.py`

```python
# containers/apps.py

from django.apps import AppConfig


class ContainersConfig(AppConfig):
    # ...
    verbose_name = "Containers"
    # ...
```

### `containers/models.py`

```python
# containers/models.py

from django.db import models


class Container(models.Model):
    """
    Model definition for Container. This model can be sub-classed by other models to add functionality.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Container"
        verbose_name_plural = "Containers"
```

### `containers/admin.py`

```python
# containers/admin.py

from django.contrib import admin
from .models import Container


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    ordering = ["name"]
```

### `containers/urls.py`

```python
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
```

### `containers/views.py`

```python
# containers/views.py

from django.shortcuts import render
from django.views.generic import ListView

from .models import Container


class ContainerListView(ListView):
    """
    Class-based `ListView` for the `containers.Container` model.
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
```

### `containers/templates/containers/container_list.html`

```html
{% comment %} containers/templates/containers/container_list.html {% endcomment %}

<h1>Containers</h1>

{% for container in container_list %}
<h2>{{ container.name }}</h2>
<p>{{ container.description }}</p>
{% endfor %}
```
