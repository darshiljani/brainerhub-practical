# Generated by Django 4.2.11 on 2024-03-23 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_employee_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
