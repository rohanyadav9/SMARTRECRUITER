# Generated by Django 5.0.2 on 2024-04-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employe',
            name='qualification',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='employe',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
