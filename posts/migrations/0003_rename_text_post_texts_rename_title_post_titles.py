# Generated by Django 4.0.4 on 2022-07-12 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='texts',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titles',
        ),
    ]