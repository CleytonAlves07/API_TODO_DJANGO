from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_fineshed = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
