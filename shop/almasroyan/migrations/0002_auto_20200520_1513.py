# Generated by Django 3.0.6 on 2020-05-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almasroyan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=15),
        ),
    ]
