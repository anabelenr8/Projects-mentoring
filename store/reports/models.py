from django.db import models

from store.common.models import ProjectModel


class Report(ProjectModel):
    text = models.TextField()
