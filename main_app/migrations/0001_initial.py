# Generated by Django 3.1.7 on 2021-03-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=80)),
                ('name', models.CharField(default='', max_length=80)),
                ('description', models.CharField(default='', max_length=300)),
                ('image', models.BinaryField(null=True)),
            ],
        ),
    ]
