# Generated by Django 4.0.3 on 2022-05-27 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_comment_refrence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='refrence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.comment'),
        ),
    ]
