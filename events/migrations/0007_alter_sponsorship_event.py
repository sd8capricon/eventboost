# Generated by Django 4.2.16 on 2024-09-06 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_remove_event_sponsors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='event',
            field=models.ForeignKey(limit_choices_to={'status': 'open'}, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
    ]
