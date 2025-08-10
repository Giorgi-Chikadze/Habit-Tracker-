from rest_framework import serializers
from habits.models import Habit, HabitLog

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency', 'created_at', 'start_date']



class HabitLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitLog
        fields = '__all__'

    
    def validate_habit(self, value):
        if not value.user == self.context['request'].user:
            raise serializers.ValidationError("You Have Not Created Such Habit")
        return value
        
    def validate(self, data):
        habit = data.get('habit')
        date = data.get('date')

        qs = HabitLog.objects.filter(habit=habit, date=date)

        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

            
        if qs.exists():
            raise serializers.ValidationError("You Already Logged This Habit For This Date")
        return data
        