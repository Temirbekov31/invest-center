# Generated by Django 4.0.4 on 2022-07-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0027_alter_addproject_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproject',
            name='group',
            field=models.CharField(choices=[('energy', 'energy'), ('production', 'production'), ('commerce', 'commerce'), ('it', 'it'), ('placeofbirth', 'placeofbirth')], max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='region',
            field=models.CharField(choices=[('Talas', 'Talas'), ('Osh', 'Osh'), ('Jalal-abad', 'Jalal-abad'), ('Batken', 'Batken'), ('Chuy', 'Chuy'), ('Naryn', 'Naryn'), ('Issyk-kul', 'Issyk-kul')], max_length=20),
        ),
    ]