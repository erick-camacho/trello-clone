from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        queryset = Card.objects.filter(list_id=self.kwargs["pk"])
        return queryset
    