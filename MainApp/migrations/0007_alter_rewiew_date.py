# Generated by Django 5.1.3 on 2025-03-20 16:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_rewiew_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewiew',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
