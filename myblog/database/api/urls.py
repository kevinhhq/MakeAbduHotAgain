from database.api.views import FoodViewSet, DietPlanViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'foods', FoodViewSet, basename='foods')
router.register(r'plans', DietPlanViewSet, basename='plans')
urlpatterns = router.urls