# Generated by Django 3.2.3 on 2021-06-07 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]