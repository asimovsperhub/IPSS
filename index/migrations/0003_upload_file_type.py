# Generated by Django 2.2.5 on 2019-10-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='file_type',
            field=models.CharField(choices=[(1, 'Windows'), (2, 'Linux'), (3, 'Android')], default=1, max_length=20, verbose_name='安装包类型'),
        ),
    ]
