# Generated by Django 3.1.7 on 2021-03-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food01',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food01',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food02',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food02',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food03',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food03',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food04',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food04',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food05',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food05',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food06',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food06',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food07',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food07',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food08',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food08',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food09',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food09',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food10',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food10',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food11',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food11',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food12',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food12',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food13',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food13',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food14',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food14',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food15',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food15',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food16',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food16',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food17',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food17',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food18',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food18',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food19',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food19',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food20',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food20',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Food21',
            fields=[
                ('foodid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('foodname', models.CharField(blank=True, max_length=128, null=True)),
                ('kcal', models.BigIntegerField(blank=True, null=True)),
                ('carbohydrate', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('protein', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
                ('fat', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'food21',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FoodTypeList',
            fields=[
                ('typeid', models.CharField(max_length=26, primary_key=True, serialize=False)),
                ('typename', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'food_type_list',
                'managed': True,
            },
        ),
    ]