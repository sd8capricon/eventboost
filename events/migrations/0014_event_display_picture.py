# Generated by Django 4.2.16 on 2024-09-21 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_rename_attendee_count_event_expected_attendee_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='display_picture',
            field=models.ImageField(blank=True, null=True, upload_to='events/'),
        ),
    ]
