# Generated by Django 2.1.5 on 2019-02-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20190201_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='desc',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='sales',
            name='taxes',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]