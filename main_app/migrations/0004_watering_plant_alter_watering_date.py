# Generated by Django 4.0 on 2022-01-01 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_watering'),
    ]

    operations = [
        migrations.AddField(
            model_name='watering',
            name='plant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.plant'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='watering',
            name='date',
            field=models.DateField(verbose_name='Watering Date'),
        ),
    ]
