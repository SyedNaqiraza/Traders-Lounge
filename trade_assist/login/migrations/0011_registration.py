# Generated by Django 2.0 on 2019-03-19 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20190319_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.ManyToManyField(to='login.Company')),
            ],
        ),
    ]
