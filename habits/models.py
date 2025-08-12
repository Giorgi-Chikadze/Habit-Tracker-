from django.db import models


class Habit(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('custom', 'Custom'),
    ]



    user = models.ForeignKey('users.User', related_name='habits', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=255, choices=FREQUENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()



class HabitLog(models.Model):
    habit = models.ForeignKey('Habit', related_name='habit_logs', on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField()
    note = models.TextField(blank=True)


class Streak(models.Model):
    habit = models.ForeignKey('Habit', related_name='streak', on_delete=models.CASCADE)
    current_streak = models.IntegerField()
    longest_streak = models.IntegerField()
    last_completed_date = models.DateField(null=True, blank=True)





