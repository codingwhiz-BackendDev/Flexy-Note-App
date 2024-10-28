# Generated by Django 4.1.4 on 2023-08-01 23:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0004_alter_alarm_songs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
