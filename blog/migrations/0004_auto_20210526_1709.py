# Generated by Django 3.1.4 on 2021-05-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like',
            field=models.IntegerField(),
        ),
    ]
