# Generated by Django 3.1.1 on 2021-02-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
