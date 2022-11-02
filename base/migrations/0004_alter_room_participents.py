# Generated by Django 4.1.1 on 2022-09-23 12:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_alter_room_options_room_participents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='participents',
            field=models.ManyToManyField(blank=True, related_name='participents', to=settings.AUTH_USER_MODEL),
        ),
    ]
