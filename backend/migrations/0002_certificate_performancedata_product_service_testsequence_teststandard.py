# Generated by Django 3.0.4 on 2020-04-06 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('model_number', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=20)),
                ('cell_technology', models.CharField(max_length=20)),
                ('cell_manufacturer', models.CharField(max_length=20)),
                ('number_of_cells', models.IntegerField()),
                ('number_of_cells_in_series', models.IntegerField()),
                ('number_of_series_strings', models.IntegerField()),
                ('number_of_diodes', models.IntegerField()),
                ('product_length', models.FloatField()),
                ('product_width', models.FloatField()),
                ('product_weight', models.FloatField()),
                ('superstrate_type', models.CharField(max_length=20)),
                ('superstrate_manufacturer', models.CharField(max_length=20)),
                ('substrate_type', models.CharField(max_length=20)),
                ('substrate_manufacturer', models.CharField(max_length=20)),
                ('frame_type', models.CharField(max_length=20)),
                ('frame_adhesive', models.CharField(max_length=20)),
                ('encapsulant_type', models.CharField(max_length=20)),
                ('encapsulant_manufacturer', models.CharField(max_length=20)),
                ('junction_box_type', models.CharField(max_length=20)),
                ('junction_box_manufacturer', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestStandard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('is_fl_required', models.BooleanField()),
                ('fl_frequency', models.FloatField()),
                ('standard_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.TestStandard')),
            ],
        ),
        migrations.CreateModel(
            name='PerformanceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_system_voltage', models.FloatField()),
                ('voc', models.FloatField()),
                ('isc', models.FloatField()),
                ('vmp', models.FloatField()),
                ('imp', models.FloatField()),
                ('pmp', models.FloatField()),
                ('ff', models.FloatField()),
                ('model_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product')),
                ('sequence_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.TestSequence')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_number', models.IntegerField()),
                ('issue_date', models.DateField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Location')),
                ('model_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Product')),
                ('standard_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.TestStandard')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
