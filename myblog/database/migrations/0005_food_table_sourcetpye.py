# Generated by Django 2.1.7 on 2019-03-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20190323_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_table',
            name='SourceTpye',
            field=models.CharField(default='Protein', max_length=15),
            preserve_default=False,
        ),
    ]
