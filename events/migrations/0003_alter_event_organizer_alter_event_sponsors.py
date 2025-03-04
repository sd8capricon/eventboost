# Generated by Django 4.2.16 on 2024-09-05 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_options_alter_account_managers_and_more'),
        ('events', '0002_alter_event_organizer_alter_event_sponsors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='event_organizer', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(blank=True, related_name='event_sponsor', to='accounts.account'),
        ),
    ]
