# Generated by Django 3.2 on 2021-08-06 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TMS_App', '0003_tickets_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='connection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TMS_App.signup'),
        ),
    ]