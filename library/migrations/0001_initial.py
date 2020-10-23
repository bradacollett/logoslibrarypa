# Generated by Django 3.0 on 2020-10-23 00:27

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
                ('book_name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('book_description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('awards', models.TextField()),
                ('isbn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magazine_name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('magazine_description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('series', models.TextField()),
                ('quantity', models.IntegerField()),
                ('movie_description', models.TextField()),
            ],
        ),
    ]
