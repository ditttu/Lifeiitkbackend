# Generated by Django 2.2.3 on 2019-07-28 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('user', models.ManyToManyField(related_name='tokens', to='users.User')),
            ],
        ),
    ]
