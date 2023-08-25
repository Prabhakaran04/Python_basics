# Generated by Django 4.2.4 on 2023-08-24 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('number_of_pages', models.IntegerField()),
                ('published_date', models.DateField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
