# Generated by Django 3.2 on 2022-04-09 03:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_alter_note_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='note',
            table='Notes',
        ),
    ]
