# Generated by Django 2.2.2 on 2019-06-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0004_auto_20190621_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='category',
            field=models.CharField(max_length=250),
        ),
    ]
