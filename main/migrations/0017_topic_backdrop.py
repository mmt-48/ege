# Generated by Django 3.1.5 on 2022-11-23 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_smailic'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='backdrop',
            field=models.ImageField(default='', upload_to='smile'),
        ),
    ]
