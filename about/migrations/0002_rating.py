# Generated by Django 5.1.2 on 2024-11-09 09:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.CharField(choices=[('RETREAT', 'Retreat'), ('MEDITATION', 'Meditation'), ('HATHA CLASS', 'Hatha Class'), ('ASHTANGA CLASS', 'Ashtanga Class')], default='RETREAT', max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='star_rating', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]