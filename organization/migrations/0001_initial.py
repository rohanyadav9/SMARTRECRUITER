# Generated by Django 5.0.2 on 2024-04-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('post', models.CharField(max_length=30)),
                ('skills', models.CharField(max_length=60)),
                ('language', models.CharField(max_length=60)),
                ('experience', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=50)),
                ('about', models.TextField()),
            ],
        ),
    ]
