# Generated by Django 4.0 on 2023-05-07 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cpovc_help', '0001_initial'),
        ('cpovc_registry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovcdownloads',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_registry.regperson'),
        ),
    ]
