from database.api.views import FoodViewSet, DietPlanViewSet, UserProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'foods', FoodViewSet, basename='foods')
router.register(r'plans', DietPlanViewSet, basename='plans')
router.register(r'user', UserProfileViewSet, basename = 'users')
urlpatterns = router.urls