# Generated by Django 3.2.3 on 2021-05-29 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ChitietSach', '0022_auto_20210529_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('chuong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ChitietSach.chuong')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]