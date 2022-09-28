# Generated by Django 4.0.4 on 2022-06-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproject', '0009_alter_addproject_group_alter_addproject_lang_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('add1', models.CharField(max_length=300)),
                ('add2', models.CharField(max_length=300)),
                ('zipC', models.IntegerField()),
                ('state', models.CharField(default=None, max_length=150)),
                ('first_name', models.CharField(default=None, max_length=123)),
                ('last_name', models.CharField(default=None, max_length=123)),
                ('email', models.EmailField(default=None, max_length=123)),
                ('phone', models.IntegerField(default=None)),
                ('image', models.ImageField(default=None, upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='addproject',
            name='group',
            field=models.CharField(choices=[('energy', 'energy'), ('commerce', 'commerce'), ('placeofbirth', 'placeofbirth'), ('production', 'production'), ('it', 'it')], max_length=20),
        ),
        migrations.AlterField(
            model_name='addproject',
            name='region',
            field=models.CharField(choices=[('Chuy', 'Chuy'), ('Issyk-kul', 'Issyk-kul'), ('Batken', 'Batken'), ('Jalal-abad', 'Jalal-abad'), ('Naryn', 'Naryn'), ('Osh', 'Osh'), ('Talas', 'Talas')], max_length=20),
        ),
    ]
