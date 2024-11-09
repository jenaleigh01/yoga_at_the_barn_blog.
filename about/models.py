from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


CHOICES = (
    ('RETREAT', 'Retreat'),
    ('MEDITATION', 'Meditation'),
    ('HATHA CLASS', 'Hatha Class'),
    ('ASHTANGA CLASS', 'Ashtanga Class')
)

class Rating(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="star_rating", null=True
    )
    experience = models.CharField(max_length=200, choices = CHOICES, default='RETREAT')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"by {self.author}"
