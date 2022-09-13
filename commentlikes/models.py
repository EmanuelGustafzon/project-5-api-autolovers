from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment


class Commentlikes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name='commentlikes', on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'comment']
 
    def __str__(self):
        return f'{self.owner} {self.comment}'
