# Generated by Django 2.0 on 2019-03-19 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20190320_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.Company'),
        ),
    ]
