# Generated by Django 3.2.6 on 2021-09-05 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppanMedia', '0002_blogpost_category_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
