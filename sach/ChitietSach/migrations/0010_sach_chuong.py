# Generated by Django 3.2.3 on 2021-05-21 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChitietSach', '0009_auto_20210521_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='sach',
            name='chuong',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ChitietSach.chuong'),
        ),
    ]
