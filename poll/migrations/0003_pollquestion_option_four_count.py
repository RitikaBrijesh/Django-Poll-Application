# Generated by Django 3.1.14 on 2022-08-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20220825_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='pollquestion',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
    ]