# Generated by Django 4.1.1 on 2022-10-16 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Second', '0006_yyzz'),
    ]

    operations = [
        migrations.CreateModel(
            name='GZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]