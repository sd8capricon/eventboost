# Generated by Django 4.2.16 on 2024-09-15 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_event_attendee_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='attendee_count',
            new_name='expected_attendee_count',
        ),
    ]