from rest_framework import routers
from .views import CardViewSet

router = routers.DefaultRouter()
router.register('lists/<int:pk>/cards', CardViewSet, basename='list_cards')
urlpatterns = router.urls