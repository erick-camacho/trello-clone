from rest_framework import viewsets
from .models import List
from .serializers import ListSerializer


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer

    def get_queryset(self):
        queryset = List.objects.filter(board_id=self.kwargs["pk"])
        return queryset
