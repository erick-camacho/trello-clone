from rest_framework import routers
from .views import ListViewSet

router = routers.DefaultRouter()
router.register('boards/<int:pk>/lists', ListViewSet, basename='board_lists')
urlpatterns = router.urls