# Generated by Django 2.2.3 on 2019-07-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_match',
            name='short_url',
            field=models.TextField(),
        ),
    ]
