from django.db import models

class ToDo(models.Model):
    topic = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.topic
