from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import HabitLog, Streak

@receiver(post_save, sender=HabitLog)
def update_streak(sender, instance, created, **kwargs):
    if not created or not instance.completed:
        return 
    
    today = instance.date
    streak, _ = Streak.objects.get_or_create(
        habit=instance.habit,
        defaults={
            "current_streak":0,
            "longest_streak":0,
            "last_completed_date":None
        }
    )

    if streak.last_completed_date is None:
        streak.current_streak = 1
    else:
        days_diff = (today - streak.last_completed_date).days
        if days_diff == 1:
            streak.current_streak += 1
        elif days_diff > 1:
            streak.current_streak = 1
        
    if streak.current_streak > streak.longest_streak:
        streak.longest_streak = streak.current_streak
        
    streak.last_completed_date = today
    streak.save()