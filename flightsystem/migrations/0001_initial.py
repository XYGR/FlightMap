# Generated by Django 3.0.8 on 2020-07-31 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=12)),
                ('city_code', models.CharField(max_length=6)),
            ],
        ),
    ]
