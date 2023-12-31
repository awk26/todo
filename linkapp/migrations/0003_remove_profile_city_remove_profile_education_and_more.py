# Generated by Django 4.2.3 on 2023-07-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkapp', '0002_alter_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profession',
        ),
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Complete', 'complete'), ('Pending', 'pending')], default=True, max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default=True, max_length=300),
        ),
    ]
