# Generated by Django 3.1.4 on 2022-10-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produktuak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=255)),
                ('prezioa', models.CharField(max_length=255)),
                ('iraungipenData', models.DateField(max_length=255)),
            ],
        ),
    ]