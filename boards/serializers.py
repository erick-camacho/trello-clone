from rest_framework import serializers
from .models import Board
from lists.serializers import ListSerializer


class BoardSerializer(serializers.ModelSerializer):
  lists = ListSerializer(many=True, read_only=True, required=False)
  members = serializers.PrimaryKeyRelatedField(many=True, required=False, read_only=True)
  owner = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = Board
    fields = '__all__'
