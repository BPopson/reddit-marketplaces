# Generated by Django 2.2.4 on 2019-09-04 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MarketplacesForReddit', '0002_auto_20190903_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='author_flair_text',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='link_flair_css_class',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='link_flair_text',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
