# Generated by Django 3.2.4 on 2021-06-10 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210526_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModernBlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btitle', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=50)),
                ('coverimg', models.ImageField(upload_to='blogImages')),
                ('img1', models.ImageField(upload_to='blogImages')),
                ('img2', models.ImageField(upload_to='blogImages')),
                ('img3', models.ImageField(upload_to='blogImages')),
                ('img4', models.ImageField(upload_to='blogImages')),
                ('img5', models.ImageField(upload_to='blogImages')),
                ('img6', models.ImageField(upload_to='blogImages')),
                ('img7', models.ImageField(upload_to='blogImages')),
                ('desc1', models.TextField()),
                ('desc2', models.TextField()),
                ('desc3', models.TextField()),
                ('desc4', models.TextField()),
                ('desc5', models.TextField()),
                ('desc6', models.TextField()),
                ('desc7', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
