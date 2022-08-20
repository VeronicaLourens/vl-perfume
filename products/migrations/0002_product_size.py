# Generated by Django 3.2 on 2022-08-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('30ml', '30ml'), ('50ml', '50ml'), ('75ml', '75ml'), ('100ml', '100ml')], default='', max_length=12),
        ),
    ]