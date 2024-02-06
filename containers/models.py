from django.db import models


class Container(models.Model):
    """
    Model definition for Container. This model will be sub-classed by other models to add functionality.
    """

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Container"
        verbose_name_plural = "Containers"
