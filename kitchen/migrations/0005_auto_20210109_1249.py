# Generated by Django 2.2.10 on 2021-01-09 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0004_auto_20210107_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen_base',
            name='detail',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kitchen_base',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]
