from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    new_colum = models.TextField()

    def __str__(self):
        return f"{self.name} {self.subject}"
