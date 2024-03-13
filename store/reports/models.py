import uuid

from django.db import models


class TimestampedModel(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_on = models.DateTimeField(auto_now=True)


class ProjectModel(TimestampedModel):
    class Meta:
        abstract = True

    uid = models.UUIDField(unique=True, null=False, default=uuid.uuid4)


class Survey(ProjectModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Question(ProjectModel):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)


class Choice(ProjectModel):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


class Response(ProjectModel):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_choices = models.ManyToManyField(Choice, blank=True)
    user_text = models.TextField(blank=True, null=True)


class Report(ProjectModel):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    responses = models.ManyToManyField(Response)
    generated_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
