# Generated by Django 3.1.5 on 2023-03-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_topic_mett1'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='mett2',
            field=models.IntegerField(default=0),
        ),
    ]
