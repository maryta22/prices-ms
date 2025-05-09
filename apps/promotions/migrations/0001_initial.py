# Generated by Django 5.2 on 2025-05-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('products', models.ManyToManyField(related_name='promotions', to='products.product')),
                ('stores', models.ManyToManyField(related_name='promotions', to='stores.store')),
            ],
        ),
    ]
