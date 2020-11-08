# Generated by Django 2.0 on 2019-03-19 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0017_auto_20190320_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='user',
        ),
        migrations.AddField(
            model_name='registration',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
