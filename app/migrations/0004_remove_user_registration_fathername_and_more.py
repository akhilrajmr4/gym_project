# Generated by Django 4.0.2 on 2022-05-24 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_achievement_batch_expense_machine_workout_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_registration',
            name='fathername',
        ),
        migrations.RemoveField(
            model_name='user_registration',
            name='mothername',
        ),
    ]
