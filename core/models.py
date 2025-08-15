from django.db import models
from django.utils import timezone  # ✅ Add this line

class Confession(models.Model):
    MOOD_CHOICES = [
        ('😊', 'Happy'),
        ('😢', 'Sad'),
        ('😰', 'Anxious'),
        ('😤', 'Frustrated'),
        ('🤔', 'Confused'),
        ('❤️', 'Loved'),
    ]
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0)
    is_trending = models.BooleanField(default=False)  # Add this field

    def __str__(self):
        return f"{self.message[:50]}..."
    

class Reply(models.Model):
    confession = models.ForeignKey(Confession, related_name='replies', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]

        