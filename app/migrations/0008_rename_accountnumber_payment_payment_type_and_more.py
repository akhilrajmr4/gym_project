# Generated by Django 4.0.2 on 2022-06-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_user_registration_admission_rate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='accountnumber',
            new_name='payment_type',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='bank',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='ifse',
        ),
        migrations.AddField(
            model_name='payment',
            name='net_due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
