# Generated by Django 5.0.1 on 2024-04-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='short_description',
            field=models.CharField(blank=True, default=None, max_length=127, null=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='tg_id',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
