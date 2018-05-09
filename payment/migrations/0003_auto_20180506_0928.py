# Generated by Django 2.0.2 on 2018-05-06 09:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20180415_0944'),
        ('payment', '0002_auto_20180504_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='subscription',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='SubscriptionTransactions', to='store.SubscriptionModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
