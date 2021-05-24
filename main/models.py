from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Todo(models.Model):
    text = models.CharField(max_length=280)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
        
