# Generated by Django 3.2.3 on 2021-05-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChitietSach', '0013_auto_20210524_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Danhmuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('danhmuc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tacgia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tacgia', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Theloai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thloai', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
