# Generated by Django 3.2.5 on 2021-07-17 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_about_slogan'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='fb_link',
            field=models.CharField(max_length=180, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='github_link',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.CharField(max_length=255, null=True),
        ),
    ]