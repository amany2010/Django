# Generated by Django 4.0 on 2022-01-02 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS', '0004_feedback_rename_credicards_creditcards'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
