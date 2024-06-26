# Generated by Django 4.0.8 on 2024-06-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_lecturer',
            field=models.BooleanField(default=False, verbose_name='Преподаватель'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_student',
            field=models.BooleanField(default=False, verbose_name='Обучающийся'),
        ),
    ]
