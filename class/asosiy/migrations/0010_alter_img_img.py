# Generated by Django 4.2.1 on 2023-05-12 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0009_alter_img_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.FileField(null=True, upload_to='ava'),
        ),
    ]
