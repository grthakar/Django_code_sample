# Generated by Django 3.0.3 on 2020-05-20 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=264)),
                ('lastname', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
