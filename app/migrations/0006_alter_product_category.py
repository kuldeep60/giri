# Generated by Django 5.0.3 on 2024-11-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('V', 'Vegetable'), ('F', 'Fruits'), ('TV', 'Top Vegetable'), ('BV', 'Bottom Vegetable')], max_length=2),
        ),
    ]
