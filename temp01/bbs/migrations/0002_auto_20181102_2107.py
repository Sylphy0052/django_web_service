# Generated by Django 2.2.dev20181101005010 on 2018-11-02 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='massage',
            new_name='message',
        ),
    ]
