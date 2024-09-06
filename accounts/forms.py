from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


class RegistrationForm(UserCreationForm):
    ACCOUNT_CHOICES = (("organizer", "Organizer"), ("sponsor", "Sponsor"))

    account_type = forms.ChoiceField(choices=ACCOUNT_CHOICES)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "account_type",
            "description",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            Account.objects.create(
                user=user,
                is_organizer=self.cleaned_data.get("account_type") == "organizer",
                is_sponsor=self.cleaned_data.get("account_type") == "sponsor",
                description=self.cleaned_data.get("description"),
            )
