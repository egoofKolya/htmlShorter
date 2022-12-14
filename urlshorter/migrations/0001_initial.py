# Generated by Django 4.1.3 on 2022-11-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('short_id', models.SlugField(max_length=6, primary_key=True, serialize=False)),
                ('httpurl', models.URLField()),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('days', models.IntegerField(default=90)),
            ],
        ),
    ]
