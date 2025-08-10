from django.urls import path, include
from habits.views import HabitViewSet, HabitLogViewSet



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("habits" , HabitViewSet)
router.register("habit_logs", HabitLogViewSet)




urlpatterns = [
    path('', include(router.urls))
]