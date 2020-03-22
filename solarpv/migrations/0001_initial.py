# Generated by Django 3.0.4 on 2020-03-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('username', models.CharField(max_length=8, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('prefix', models.CharField(choices=[{'Mr.', 'Mister'}, {'Mrs.', 'Misses'}, {'Ms.', 'Miss'}, {'Dr.', 'Doctor'}], max_length=6)),
                ('firstname', models.CharField(max_length=45)),
                ('middlename', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('job_title', models.CharField(max_length=45)),
                ('officephone', models.CharField(max_length=12)),
                ('cellphone', models.CharField(max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
