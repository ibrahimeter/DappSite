# Generated by Django 3.2.6 on 2021-08-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Annual Operation Report', max_length=100, null='true')),
                ('pdffile', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(blank=1, choices=[('GT1', 'GT1'), ('GT2', 'GT2'), ('ST', 'ST')], max_length=5, null=True)),
                ('MainDesc', models.CharField(blank=True, max_length=100, null=True)),
                ('EOH', models.DecimalField(blank=True, decimal_places=4, max_digits=10, null=True)),
                ('MainDate', models.DateField(null=True)),
                ('Firm', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
