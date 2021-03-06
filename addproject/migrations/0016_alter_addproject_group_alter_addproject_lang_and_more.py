# Generated by Django 4.0.4 on 2022-07-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0015_alter_addproject_group_alter_addproject_lang_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproject',
            name='group',
            field=models.CharField(choices=[('production', 'production'), ('commerce', 'commerce'), ('placeofbirth', 'placeofbirth'), ('energy', 'energy'), ('it', 'it')], max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='lang',
            field=models.CharField(choices=[('ru', 'ru'), ('en', 'en')], default='ru', max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='region',
            field=models.CharField(choices=[('Osh', 'Osh'), ('Issyk-kul', 'Issyk-kul'), ('Naryn', 'Naryn'), ('Talas', 'Talas'), ('Jalal-abad', 'Jalal-abad'), ('Batken', 'Batken'), ('Chuy', 'Chuy')], max_length=20),
        ),
    ]
