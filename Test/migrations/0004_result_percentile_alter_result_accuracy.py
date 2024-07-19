# Generated by Django 5.0.6 on 2024-07-13 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0003_alter_result_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='Percentile',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='Accuracy',
            field=models.FloatField(),
        ),
    ]
