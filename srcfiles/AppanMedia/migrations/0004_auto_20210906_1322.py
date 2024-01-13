# Generated by Django 3.2.6 on 2021-09-06 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppanMedia', '0003_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='contents',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content1',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content2',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content3',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content4',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='content5',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head3',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head4',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='head5',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image4',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='image5',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='main_content',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
