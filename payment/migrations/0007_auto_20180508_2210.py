# Generated by Django 2.0.2 on 2018-05-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_transactions_subscription_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='knettransactions',
            name='paid',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gotaptransactions',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='subscription_updated',
            field=models.BooleanField(default=False),
        ),
    ]