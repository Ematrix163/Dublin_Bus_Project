# Generated by Django 2.0.6 on 2018-07-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_main', models.CharField(max_length=30)),
                ('dt', models.DurationField(max_length=30)),
            ],
        ),
    ]
