# Generated by Django 3.2.3 on 2021-06-04 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210531_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='url',
            new_name='file',
        ),
    ]
