





# add model with foregin key 

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField(blank=True) # some one can keep empty space
    created = models.DateTimeField(auto_now_add=True) # automatically create time # not editable
    datecompleted = models.DateTimeField(null=True)  # different field same this to blank
    important = models.BooleanField(default=False)

    # navigation to user
        # one user can make many todo
        # one todo belongs to one user

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} todo'
