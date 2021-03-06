# Generated by Django 2.1.5 on 2019-02-10 21:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('currency', models.CharField(max_length=3)),
                ('buy', models.DecimalField(decimal_places=3, max_digits=10)),
                ('sell', models.DecimalField(decimal_places=3, max_digits=10)),
                ('variation', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
