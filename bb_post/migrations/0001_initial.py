# Generated by Django 2.1.5 on 2019-03-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]