# Generated by Django 3.2 on 2022-03-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]