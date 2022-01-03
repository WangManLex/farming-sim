# Generated by Django 4.0 on 2022-01-03 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main_app', '0007_plant_fertilizers'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
