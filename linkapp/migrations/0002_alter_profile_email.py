# Generated by Django 4.2.3 on 2023-07-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
