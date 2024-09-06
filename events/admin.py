from django.contrib import admin
from django import forms
from .models import Event, SponsorshipTier, Sponsorship

# Register your models here.
admin.site.register(Event)
admin.site.register(SponsorshipTier)
admin.site.register(Sponsorship)
