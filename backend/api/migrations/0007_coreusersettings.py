# Generated by Django 2.0.6 on 2018-08-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_dublinbusschedulecurrent'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoreUsersettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routeid', models.CharField(max_length=20)),
                ('direction', models.CharField(max_length=200)),
                ('originstop', models.CharField(max_length=200)),
                ('destinationstop', models.CharField(max_length=200)),
                ('journeyname', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'core_usersettings',
                'managed': False,
            },
        ),
    ]
