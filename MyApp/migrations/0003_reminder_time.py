# Generated by Django 4.2.5 on 2023-11-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_remove_reminder_category_remove_reminder_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='Time',
            field=models.TimeField(default='12:00'),
            preserve_default=False,
        ),
    ]
