# Generated by Django 3.2.3 on 2021-05-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChitietSach', '0003_auto_20210519_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='sach',
            name='noidung',
            field=models.TextField(blank=True, null=True),
        ),
    ]