# Generated by Django 3.2.5 on 2022-03-03 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rphusers', '0004_alter_userprofile_social_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='firstname <django.db.models.fields.UUIDField>', max_length=100),
        ),
    ]
