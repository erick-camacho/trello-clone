from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.mail import send_mail

from .models import Board
from django.contrib.auth.models import User, Group
from .serializers import BoardSerializer
from users.serializers import UserSerializer
from trello.serializers import EmailSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Board.objects.filter(owner=self.request.user)
        return queryset


    @action(detail=True, methods=['POST'])
    def invite_member(self, request, pk=None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            send_mail(
                'Board invitation',
                'Click link to accept invitation ... /accept_invitation?email=''',
                'ercamdev@gmail.com',
                [email],
                fail_silently=False,
            )
            return Response(f'Email sent to {email} successfully.', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['GET'])
    def accept_invitation(self, request, pk=None):
        email = request.query_params['email']
        user = User.objects.get(email=email)
        # agregar al grupo
        return Response('Member added successfully', status=status.HTTP_200_OK)

