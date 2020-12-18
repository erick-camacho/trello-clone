from django.urls import path
from .views import CreateComment

urlpatterns = [
    path('cards/<int:pk>/comments', CreateComment.as_view(), name="create_comment")
]
