# Generated by Django 3.0.3 on 2020-07-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
    ]
