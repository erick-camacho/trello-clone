from rest_framework import serializers
from .models import Board
from lists.serializers import ListSerializer


class BoardSerializer(serializers.ModelSerializer):
  lists = ListSerializer(many=True, read_only=True, required=False)

  class Meta:
    model = Board
    fields = '__all__'
