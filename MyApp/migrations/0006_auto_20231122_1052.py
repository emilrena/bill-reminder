# Generated by Django 3.2.21 on 2023-11-22 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_auto_20231122_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Reply',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='description',
            field=models.CharField(max_length=300),
        ),
    ]
