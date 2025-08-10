from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import ListModelMixin
from habits.models import Habit, HabitLog
from habits.serializers import HabitSerializer, HabitLogSerializer
from rest_framework.permissions import IsAuthenticated

class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class HabitLogViewSet(ModelViewSet):
    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(habit__user=self.request.user)




