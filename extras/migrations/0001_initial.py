# Generated by Django 4.2.2 on 2023-07-24 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingCost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_cost', models.DecimalField(decimal_places=2, default=20.0, max_digits=5)),
            ],
        ),
    ]
