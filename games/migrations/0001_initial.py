# Generated by Django 4.1 on 2023-03-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.TextField()),
                ('game', models.TextField()),
                ('score', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]