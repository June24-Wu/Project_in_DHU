# Generated by Django 3.1.4 on 2021-03-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_login', '0004_auto_20210315_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbloodpressure',
            name='bloodpressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userbloodsugar',
            name='bloodsugar',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userheight',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userwaist',
            name='waist',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userweight',
            name='weight',
            field=models.IntegerField(),
        ),
    ]