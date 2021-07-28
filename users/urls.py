from rest_framework import routers, urlpatterns
from .views import UserViewSet, PlayerViewSet

router = routers.DefaultRouter()
router.register(r'accounts', UserViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = router.urls