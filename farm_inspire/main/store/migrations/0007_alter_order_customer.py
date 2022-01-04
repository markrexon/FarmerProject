# Generated by Django 3.2.9 on 2021-12-10 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_addproducts_category'),
        ('store', '0006_alter_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.customer'),
        ),
    ]
