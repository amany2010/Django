# Generated by Django 4.0 on 2021-12-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewAccounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('password', models.IntegerField()),
                ('phoneNum', models.TextField()),
                ('maile', models.TextField()),
                ('national_id', models.TextField()),
                ('balanc', models.IntegerField()),
                ('account_type', models.CharField(max_length=10)),
            ],
        ),
    ]
