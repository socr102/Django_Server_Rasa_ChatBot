# Generated by Django 3.1.6 on 2021-08-20 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chattracker',
            name='init_message',
            field=models.CharField(blank=True, default='', max_length=5000),
        ),
    ]
