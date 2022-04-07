# Generated by Django 4.0.3 on 2022-04-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_alter_question_answer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.CharField(choices=[('text', 'Pole Tekstowe'), ('radio', 'Pojedynczy wybor'), ('checkbox', 'Wielokrotnego wyboru'), ('Skala', 'Scale')], default='Pole Tekstowe', max_length=30),
        ),
    ]
