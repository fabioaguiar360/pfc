# Generated by Django 2.2.2 on 2019-06-21 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0006_auto_20190621_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='namem', to='categories.Category'),
        ),
    ]
