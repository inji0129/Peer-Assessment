# Generated by Django 3.0 on 2020-05-03 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20200503_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(default=0)),
                ('total_question', models.IntegerField(default=0)),
                ('total_student', models.IntegerField(default=0)),
            ],
        ),
    ]
