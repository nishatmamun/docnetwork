# Generated by Django 3.2.5 on 2021-07-31 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('offer', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
