# Generated by Django 3.1.5 on 2023-03-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_topic_mett2'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='mett3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_topic1',
            field=models.CharField(db_index=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_topic2',
            field=models.CharField(db_index=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='topic',
            name='name_topic3',
            field=models.CharField(db_index=True, default='', max_length=200),
        ),
    ]