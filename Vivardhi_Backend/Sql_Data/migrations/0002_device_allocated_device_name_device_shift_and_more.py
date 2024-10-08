# Generated by Django 5.0.7 on 2024-10-07 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sql_Data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='allocated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='device',
            name='name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='device',
            name='shift',
            field=models.CharField(default='Day', max_length=50),
        ),
        migrations.AddField(
            model_name='device',
            name='working_hours',
            field=models.CharField(default='8 hours', max_length=50),
        ),
        migrations.AlterModelTable(
            name='device',
            table='SAMPLE_DATA',
        ),
    ]
