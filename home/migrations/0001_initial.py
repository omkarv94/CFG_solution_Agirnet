# Generated by Django 3.2.13 on 2022-06-25 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('driver', models.CharField(max_length=50)),
                ('asset_duration', models.IntegerField()),
                ('rent_amount', models.IntegerField()),
            ],
            options={
                'db_table': 'asset',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FarmerActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('activity_proof', models.TextField()),
            ],
            options={
                'db_table': 'farmer_activity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FarmerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc_lat', models.CharField(max_length=50)),
                ('loc_long', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('land_size', models.FloatField()),
                ('number_seedling', models.IntegerField()),
            ],
            options={
                'db_table': 'farmer_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaterialsConsumed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('bill', models.CharField(db_collation='latin1_swedish_ci', max_length=150)),
            ],
            options={
                'db_table': 'materials_consumed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PeopleInvolved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_payable', models.IntegerField()),
                ('worker_name', models.CharField(max_length=50)),
                ('duration', models.IntegerField()),
                ('amount_paid', models.IntegerField()),
            ],
            options={
                'db_table': 'people_involved',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_material', models.CharField(max_length=50)),
                ('units', models.IntegerField()),
                ('storage_location', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'production',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField(max_length=10, unique=True)),
                ('password', models.TextField(max_length=50)),
                ('type', models.IntegerField()),
            ],
            options={
                'db_table': 'register',
                'managed': False,
            },
        ),
    ]
