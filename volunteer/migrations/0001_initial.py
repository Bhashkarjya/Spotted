# Generated by Django 2.2 on 2020-01-09 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Age', models.IntegerField()),
                ('Campaign_id', models.CharField(max_length=155)),
                ('Email', models.EmailField(max_length=254)),
                ('PhoneNumber', models.IntegerField()),
                ('Country', models.CharField(max_length=120)),
                ('State', models.CharField(max_length=120)),
                ('City', models.CharField(max_length=120)),
            ],
        ),
    ]