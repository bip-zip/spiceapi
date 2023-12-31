# Generated by Django 4.2.8 on 2023-12-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact', models.CharField(max_length=10)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
