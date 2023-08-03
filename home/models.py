from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    Model to add reviews about the lessons
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=80)
    created_on = models.DateField(auto_now=True)
    body = models.TextField(max_length=350, null=False, blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
