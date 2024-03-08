from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField()

    class Meta:
        abstract = True
