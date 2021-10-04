# Generated by Django 3.2.7 on 2021-10-04 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='disliked_by',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likes',
            name='liked_by',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
