# Generated by Django 3.2.4 on 2021-08-06 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=None),
        ),
    ]