# Generated by Django 4.1.7 on 2023-03-30 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_oder_order_rename_oderttem_orderttem_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderTtem',
            new_name='OrderItem',
        ),
    ]
