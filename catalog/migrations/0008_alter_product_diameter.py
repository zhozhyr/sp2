# Generated by Django 5.0.6 on 2024-08-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Диаметр'),
        ),
    ]
