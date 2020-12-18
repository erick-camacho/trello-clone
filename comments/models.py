from django.db import models
from django.contrib.auth.models import User
from cards.models import Card


class Comment(models.Model):
  card = models.ForeignKey(
    Card, related_name="comments", on_delete=models.CASCADE)
  message = models.TextField()
  owner = models.ForeignKey(
    User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.id
