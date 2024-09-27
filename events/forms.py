from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from events.models import Event, SponsorshipTier, Sponsorship
from accounts.models import Account


class DateInput(forms.DateInput):
    input_type = "date"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ("organizer", "sponsors", "display_picture", "brochure")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "end_date": DateInput(attrs={"class": "form-control"}),
            "start_date": DateInput(attrs={"class": "form-control"}),
            "sponsorship_deadline": DateInput(attrs={"class": "form-control"}),
            "expected_attendee_count": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, assets=False, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        if assets:
            self.fields["display_picture"] = forms.ImageField(
                required=False
            )  # Include the display_picture field
            self.fields["brochure"] = forms.FileField(
                required=False
            )  # Include the brochure field

    def save(self, commit=True, organizer_id=None):
        event = super().save(commit=False)
        if organizer_id:
            organizer = Account.objects.get(id=organizer_id)
            event.organizer = organizer
        if commit:
            event.save()
        return event


class EventAssetForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["display_picture", "brochure"]


class TierForm(forms.ModelForm):
    class Meta:
        model = SponsorshipTier
        exclude = ["event"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "benefits": forms.Textarea(attrs={"class": "form-control"}),
        }

    def save(self, commit=True, event_id=None):
        tier = super().save(commit=False)
        if event_id:
            event = Event.objects.get(id=event_id)
            tier.event = event
        if commit:
            tier.save()
        return tier


class SponsorshipForm(
    forms.ModelForm,
):

    class Meta:
        model = Sponsorship
        exclude = ["sponsor"]

    def __init__(self, *args, event_id, tier_pk, **kwargs):
        super(SponsorshipForm, self).__init__(*args, **kwargs)
        self.event = Event.objects.get(id=event_id)
        self.initial["event"] = event_id
        self.fields["event"].disabled = True
        if event_id:
            self.fields["tier"].queryset = SponsorshipTier.objects.filter(
                event=self.event
            )
        self.initial["tier"] = tier_pk

    def save(self, commit=True, spon_id=None):
        sponsorship = super().save(commit=False)
        if spon_id:
            sponsor = Account.objects.get(id=spon_id)
            sponsor.event = self.event
            sponsorship.sponsor = sponsor
        if commit:
            sponsorship.save()
        return sponsorship
