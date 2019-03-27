from database.api.views import FoodViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FoodViewSet, basename='foods')
urlpatterns = router.urls