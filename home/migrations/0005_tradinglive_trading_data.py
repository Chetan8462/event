# Generated by Django 3.0.7 on 2020-08-12 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200812_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='tradinglive',
            name='Trading_data',
            field=models.ManyToManyField(related_name='trading_details', to='home.Trading'),
        ),
    ]
