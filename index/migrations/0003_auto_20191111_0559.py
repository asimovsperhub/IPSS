# Generated by Django 2.2.5 on 2019-11-11 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20191111_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='label',
            field=models.CharField(max_length=200, verbose_name='博客标签'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=200, verbose_name='博客标题'),
        ),
    ]
