# Generated by Django 3.2 on 2022-04-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0002_book_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=11, verbose_name='作者')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
        ),
    ]
