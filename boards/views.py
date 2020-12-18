from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Board
from .serializers import BoardSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
