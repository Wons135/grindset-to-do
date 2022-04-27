# Generated by Django 3.2.8 on 2022-04-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('type', models.TextField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=0)),
            ],
        ),
    ]
