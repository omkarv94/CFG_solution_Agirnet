# Generated by Django 3.2.13 on 2022-06-25 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220626_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='uid',
            field=models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.register'),
        ),
        migrations.AddField(
            model_name='farmeractivity',
            name='uid',
            field=models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.register'),
        ),
        migrations.AddField(
            model_name='farmerdetails',
            name='uid',
            field=models.ForeignKey(db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.register'),
        ),
        migrations.AlterField(
            model_name='farmeractivity',
            name='end_date',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='farmeractivity',
            name='start_date',
            field=models.CharField(max_length=10),
        ),
    ]
