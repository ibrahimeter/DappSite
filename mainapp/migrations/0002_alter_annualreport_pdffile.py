# Generated by Django 3.2.6 on 2021-08-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annualreport',
            name='pdffile',
            field=models.FileField(upload_to='annualreport/'),
        ),
    ]
