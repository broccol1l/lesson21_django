# Generated by Django 5.0.6 on 2024-07-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_newscategory_newscategorymodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsmodel',
            name='news_image',
            field=models.FileField(blank=True, null=True, upload_to='product_image'),
        ),
    ]
