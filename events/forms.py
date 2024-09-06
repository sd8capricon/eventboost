from django import forms
from events.models import Event, SponsorshipTier
from accounts.models import Account


class DateInput(forms.DateInput):
    input_type = "date"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ["organizer", "sponsors"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "end_date": DateInput(attrs={"class": "form-control"}),
            "start_date": DateInput(attrs={"class": "form-control"}),
            "sponsorship_deadline": DateInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }

    def save(self, commit=True, organizer_id=None):
        event = super().save(commit=False)
        if organizer_id:
            organizer = Account.objects.get(id=organizer_id)
            event.organizer = organizer
        if commit:
            event.save()
        return event


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
