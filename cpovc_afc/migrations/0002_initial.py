# Generated by Django 4.0 on 2023-05-07 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cpovc_forms', '0001_initial'),
        ('cpovc_auth', '0001_initial'),
        ('cpovc_afc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='afcmain',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovccaserecord'),
        ),
        migrations.AddField(
            model_name='afcmain',
            name='created_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='cpovc_auth.appuser'),
        ),
    ]
