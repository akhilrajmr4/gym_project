# Generated by Django 4.0.2 on 2022-06-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_user_registration_select_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='net_due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
