# Generated by Django 4.0.3 on 2022-06-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_todoitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
