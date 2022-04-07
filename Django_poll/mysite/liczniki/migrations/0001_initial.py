# Generated by Django 4.0.3 on 2022-04-07 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licznik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licznik_id', models.SmallIntegerField(unique=True)),
                ('value', models.IntegerField(default=0)),
                ('data_odczytu', models.DateTimeField(auto_now=True, verbose_name='date published')),
            ],
        ),
    ]
