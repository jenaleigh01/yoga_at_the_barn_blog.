from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
CHOICES = (
    ('RETREAT', 'Retreat'),
    ('MEDITATION', 'Meditation'),
    ('HATHA CLASS', 'Hatha Class'),
    ('ASHTANGA CLASS', 'Ashtanga Class')
)

class Rating(models.Model):
    experience = models.CharField(max_length=200, choices = CHOICES, default='RETREAT')
    first_name = models.CharField(max_length=200)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
