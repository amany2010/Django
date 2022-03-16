# Generated by Django 4.0 on 2021-12-30 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMS', '0002_alter_newaccounts_balanc'),
    ]

    operations = [
        migrations.CreateModel(
            name='credicards',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phoneNum', models.TextField()),
                ('maile', models.TextField()),
                ('monthluSalary', models.IntegerField(default=0)),
                ('Age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='newaccounts',
            name='password',
            field=models.CharField(max_length=4),
        ),
    ]
