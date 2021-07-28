from rest_framework import routers, urlpatterns
from .views import TeamViewSet

router = routers.DefaultRouter()
router.register(r'', TeamViewSet)

urlpatterns = router.urls