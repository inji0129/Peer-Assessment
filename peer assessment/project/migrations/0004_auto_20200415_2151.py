# Generated by Django 3.0 on 2020-04-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='option_five',
            field=models.CharField(default='DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='poll',
            name='option_five_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poll',
            name='option_four',
            field=models.CharField(default='DEFAULT VALUE', max_length=30),
        ),
        migrations.AddField(
            model_name='poll',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
    ]
