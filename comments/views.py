from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CommentSerializer


class CreateComment(APIView):
    def post(self, request, pk):
        message = request.data.get("message")
        owner = request.user
        data = {"card": pk, "message": message, "owner": owner}
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
