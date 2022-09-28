# Generated by Django 4.0.4 on 2022-07-04 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0024_alter_addproject_group_alter_addproject_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproject',
            name='group',
            field=models.CharField(choices=[('energy', 'energy'), ('production', 'production'), ('it', 'it'), ('commerce', 'commerce'), ('placeofbirth', 'placeofbirth')], max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='region',
            field=models.CharField(choices=[('Naryn', 'Naryn'), ('Jalal-abad', 'Jalal-abad'), ('Issyk-kul', 'Issyk-kul'), ('Osh', 'Osh'), ('Chuy', 'Chuy'), ('Talas', 'Talas'), ('Batken', 'Batken')], max_length=20),
        ),
    ]
