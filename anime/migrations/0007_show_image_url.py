# Generated by Django 2.1.7 on 2019-03-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_auto_20190312_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]