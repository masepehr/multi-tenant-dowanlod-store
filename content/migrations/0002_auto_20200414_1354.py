# Generated by Django 2.2.12 on 2020-04-14 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store'),
        ),
        migrations.AddField(
            model_name='file',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Product'),
        ),
    ]
