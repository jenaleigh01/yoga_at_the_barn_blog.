from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHOICES = (
    ('RETREAT', 'Retreat'),
    ('MEDITATION', 'Meditation'),
    ('HATHA CLASS', 'Hatha Class'),
    ('ASHTANGA CLASS', 'Ashtanga Class')
)

class Rating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )
    experience = models.CharField(max_length=200, choices = CHOICES, default='RETREAT')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.rating}"
