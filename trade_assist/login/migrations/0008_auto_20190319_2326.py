# Generated by Django 2.0 on 2019-03-19 18:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0007_company_user_companies'),
    ]

    operations = [
        migrations.CreateModel(
            name='comapnies_registered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='user_companies',
        ),
        migrations.AddField(
            model_name='comapnies_registered',
            name='companies',
            field=models.ManyToManyField(to='login.Company'),
        ),
        migrations.AddField(
            model_name='comapnies_registered',
            name='user_companies',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
