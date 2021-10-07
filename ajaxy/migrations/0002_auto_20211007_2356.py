# Generated by Django 3.1 on 2021-10-07 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajaxy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=70, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]