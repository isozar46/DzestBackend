# Generated by Django 4.0.3 on 2022-05-07 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_client_first_name_remove_client_last_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offer',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='offer',
            name='latitude',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='longtitude',
            field=models.FloatField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='municipal',
            field=models.CharField(default='ain djasser', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='state',
            field=models.CharField(default='batna', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='street_adress',
            field=models.TextField(default='1st november', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='zip_code',
            field=models.CharField(default='5463', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OfferLocation',
        ),
    ]
