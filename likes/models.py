from django.db import models
from django.contrib.auth.models import User
from review.models import Review


class Reviewlikes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review, related_name='likes', on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'review']

    def __str__(self):
        return f'{self.owner} {self.review}'


