# Generated by Django 3.2.2 on 2021-05-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210515_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=1),
        ),
    ]
