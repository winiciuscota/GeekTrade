# Generated by Django 2.1.5 on 2019-02-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='buy',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='quotation',
            name='sell',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
    ]