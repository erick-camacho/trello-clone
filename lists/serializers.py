from rest_framework import serializers
from .models import List
from cards.serializers import CardSerializer


class ListSerializer(serializers.ModelSerializer):
  cards = CardSerializer(many=True, required=False)

  class Meta:
    model = List
    fields = '__all__'
