# Generated by Django 4.2.16 on 2024-09-06 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_options_alter_account_managers_and_more'),
        ('events', '0004_alter_event_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(limit_choices_to={'is_organizer': True}, on_delete=django.db.models.deletion.CASCADE, related_name='event_organizer', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_sponsor': True}, related_name='event_sponsor', to='accounts.account'),
        ),
        migrations.CreateModel(
            name='SponsorshipTier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('benfits', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorship_tier', to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('sponsor', models.ForeignKey(limit_choices_to={'is_sponsor': True}, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('tier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.sponsorshiptier')),
            ],
            options={
                'unique_together': {('sponsor', 'event', 'tier')},
            },
        ),
    ]
