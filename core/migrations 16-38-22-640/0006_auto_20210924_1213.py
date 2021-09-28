# Generated by Django 2.2.14 on 2021-09-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210923_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(blank=True,null=True,auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport wear'), ('OW', 'Outwear'), ('A', 'Accessories'), ('P', 'Phones'), ('T', 'Tools'), ('T', 'Laptops')], max_length=2),
        ),
    ]
