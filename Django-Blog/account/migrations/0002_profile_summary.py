# Generated by Django 2.2.2 on 2019-07-23 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='summary',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
