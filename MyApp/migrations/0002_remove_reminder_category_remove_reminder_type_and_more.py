# Generated by Django 4.2.5 on 2023-10-03 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='CATEGORY',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='Type',
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=100)),
                ('subcategoryname', models.CharField(max_length=100)),
                ('CATEGORY', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.category')),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='reminder',
            name='SUBCATEGORY',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MyApp.subcategory'),
            preserve_default=False,
        ),
    ]
