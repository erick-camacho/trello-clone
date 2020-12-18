from django.db import models
from django.contrib.auth.models import User, Group
from lists.models import List


class Card(models.Model):
  title = models.CharField(max_length=255)
  list = models.ForeignKey(List, related_name='cards', on_delete=models.CASCADE)
  description = models.TextField(blank=True)
  members = models.ManyToManyField(User, related_name='card_members')
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  expiration = models.DateTimeField(blank=True)
  position = models.IntegerField(null=True)

  class Meta:
    ordering = ['position']

  def __str__(self):
      return self.title
