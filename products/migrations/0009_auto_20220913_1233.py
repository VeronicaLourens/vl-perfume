# Generated by Django 3.2 on 2022-09-13 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='star_rating',
            field=models.IntegerField(choices=[('1 star', '1 star'), ('2 star', '2 star'), ('3 star', '3 star'), ('4 star', '4 star'), ('5 star', '5 star')], default='5 star'),
        ),
    ]