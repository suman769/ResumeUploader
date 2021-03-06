# Generated by Django 3.1.6 on 2021-03-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('delhi', 'Delhi'), ('mumbai', 'Mumbai')], max_length=100)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('job_city', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(upload_to='profileimg')),
                ('my_file', models.FileField(upload_to='doc')),
            ],
        ),
    ]
