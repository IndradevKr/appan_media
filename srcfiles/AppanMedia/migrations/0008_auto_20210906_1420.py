# Generated by Django 3.2.6 on 2021-09-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppanMedia', '0007_auto_20210906_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head3',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head4',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head5',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]