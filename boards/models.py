from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
  VISIBILITY_CHOICES = [
    ('Private', 'private'),
    ('Team', 'team'),
    ('Public', 'public')
  ]
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  created = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  is_favorite = models.BooleanField(default=False)
  visibility = models.CharField(max_length=6, choices=VISIBILITY_CHOICES, default='team')
  members = models.ManyToManyField(User, related_name='board_members')

  def __str__(self):
    return self.title
