# Generated by Django 3.2.7 on 2021-10-04 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_question_time_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
