# Generated by Django 3.1.3 on 2021-03-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prototype', '0004_auto_20210310_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='colour',
            field=models.CharField(choices=[('White (default)', 'white'), ('Red', 'red'), ('Blue', 'blue'), ('Yellow', 'yellow'), ('Green', 'green'), ('Purple', 'purple'), ('Orange', 'orange'), ('Pink', 'pink')], default='White (default)', max_length=15),
        ),
        migrations.AddField(
            model_name='task',
            name='colour',
            field=models.CharField(choices=[('White (default)', 'white'), ('Red', 'red'), ('Blue', 'blue'), ('Yellow', 'yellow'), ('Green', 'green'), ('Purple', 'purple'), ('Orange', 'orange'), ('Pink', 'pink')], default='White (default)', max_length=15),
        ),
    ]
