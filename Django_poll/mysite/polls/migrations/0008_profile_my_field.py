# Generated by Django 4.0.3 on 2022-03-25 14:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='my_field',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], default='item_key1', max_length=49),
        ),
    ]
