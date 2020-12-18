from django.db import models
from boards.models import Board


class List(models.Model):
  title = models.CharField(max_length=255)
  board = models.ForeignKey(Board, related_name='lists', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  position = models.IntegerField(null=True)

  class Meta:
    ordering = ['position']

  def __str__(self):
      return self.title
