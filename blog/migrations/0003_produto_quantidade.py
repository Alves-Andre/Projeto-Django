# Generated by Django 3.2.21 on 2023-09-13 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
