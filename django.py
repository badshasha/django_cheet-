from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return f"{self.title} {self.description}"
