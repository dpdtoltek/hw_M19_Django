# Generated by Django 5.1.4 on 2024-12-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_rename_name_buyer_username_buyer_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]