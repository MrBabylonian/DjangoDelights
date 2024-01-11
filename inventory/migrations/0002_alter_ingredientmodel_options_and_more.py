# Generated by Django 5.0.1 on 2024-01-11 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredientmodel',
            options={'ordering': ['-price_per_unit'], 'verbose_name': 'Ingredient'},
        ),
        migrations.AlterModelOptions(
            name='menuitemmodel',
            options={'verbose_name': 'Menu Item'},
        ),
        migrations.AlterModelOptions(
            name='purchasemodel',
            options={'verbose_name': 'Sale'},
        ),
        migrations.AlterModelOptions(
            name='reciperequirementmodel',
            options={'verbose_name': 'Recipe Requirement'},
        ),
    ]
