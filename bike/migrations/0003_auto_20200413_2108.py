# Generated by Django 3.0.5 on 2020-04-13 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_mapqueries_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapqueries',
            name='polyline',
            field=models.CharField(max_length=510),
        ),
    ]
