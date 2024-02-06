from django.contrib import admin
from .models import Container


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    # list_filter = ["name"]
    ordering = ["name"]
