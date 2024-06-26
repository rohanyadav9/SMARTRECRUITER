# Generated by Django 5.0.2 on 2024-04-14 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0002_alter_employe_name_alter_employe_qualification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('qualification', models.CharField(max_length=40)),
                ('skills', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=50)),
                ('personal_skills', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=30)),
            ],
        ),
    ]
