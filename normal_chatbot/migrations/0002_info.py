# Generated by Django 4.1.5 on 2023-01-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('normal_chatbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firsname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=12)),
            ],
        ),
    ]