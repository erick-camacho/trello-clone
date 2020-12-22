from rest_framework import serializers
from .models import Card
from comments.serializers import CommentSerializer


class CardSerializer(serializers.ModelSerializer):
  comments = CommentSerializer(many=True, required=False)
  members = serializers.PrimaryKeyRelatedField(many=True, required=False, read_only=True)
  owner = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = Card
    fields = '__all__'
