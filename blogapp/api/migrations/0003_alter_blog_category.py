# Generated by Django 3.2.4 on 2021-08-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_blog_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]
