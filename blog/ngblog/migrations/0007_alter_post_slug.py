# Generated by Django 4.1.7 on 2023-04-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngblog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True),
        ),
    ]
