# Generated by Django 3.2.3 on 2021-05-19 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChitietSach', '0004_sach_noidung'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sach',
            name='hinh',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
