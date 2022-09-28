# Generated by Django 4.0.4 on 2022-07-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0038_alter_addproject_group_alter_addproject_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproject',
            name='group',
            field=models.CharField(choices=[('it', 'it'), ('placeofbirth', 'placeofbirth'), ('energy', 'energy'), ('production', 'production'), ('commerce', 'commerce')], max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='lang',
            field=models.CharField(choices=[('ru', 'ru'), ('en', 'en')], default='ru', max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='region',
            field=models.CharField(choices=[('Talas', 'Talas'), ('Naryn', 'Naryn'), ('Batken', 'Batken'), ('Chuy', 'Chuy'), ('Osh', 'Osh'), ('Jalal-abad', 'Jalal-abad'), ('Issyk-kul', 'Issyk-kul')], max_length=20),
        ),
    ]