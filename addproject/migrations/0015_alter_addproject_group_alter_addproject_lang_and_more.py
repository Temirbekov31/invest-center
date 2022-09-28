# Generated by Django 4.0.4 on 2022-07-01 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0014_alter_addproject_group_alter_addproject_lang_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproject',
            name='group',
            field=models.CharField(choices=[('commerce', 'commerce'), ('production', 'production'), ('it', 'it'), ('energy', 'energy'), ('placeofbirth', 'placeofbirth')], max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='lang',
            field=models.CharField(choices=[('en', 'en'), ('ru', 'ru')], default='ru', max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='region',
            field=models.CharField(choices=[('Osh', 'Osh'), ('Batken', 'Batken'), ('Talas', 'Talas'), ('Chuy', 'Chuy'), ('Naryn', 'Naryn'), ('Issyk-kul', 'Issyk-kul'), ('Jalal-abad', 'Jalal-abad')], max_length=20),
        ),
    ]