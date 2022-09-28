# Generated by Django 4.0.4 on 2022-07-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0018_post_alter_addproject_group_alter_addproject_region'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AlterField(
            model_name='addproject',
            name='group',
            field=models.CharField(choices=[('placeofbirth', 'placeofbirth'), ('it', 'it'), ('production', 'production'), ('commerce', 'commerce'), ('energy', 'energy')], max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='region',
            field=models.CharField(choices=[('Chuy', 'Chuy'), ('Jalal-abad', 'Jalal-abad'), ('Issyk-kul', 'Issyk-kul'), ('Naryn', 'Naryn'), ('Osh', 'Osh'), ('Talas', 'Talas'), ('Batken', 'Batken')], max_length=20),
        ),
    ]
