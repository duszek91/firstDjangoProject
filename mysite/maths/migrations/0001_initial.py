# Generated by Django 3.2.3 on 2021-05-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(max_length=3)),
                ('arg_a', models.FloatField()),
                ('arg_b', models.FloatField()),
                ('result', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
