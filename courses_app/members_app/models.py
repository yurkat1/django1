from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    session_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username


