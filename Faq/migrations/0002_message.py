# Generated by Django 3.1.1 on 2021-02-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
