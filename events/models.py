from django.db import models
from accounts.models import Account

# Create your models here.


class Event(models.Model):
    CATEGORY_CHOICES = (
        # (value, display)
        ("open", "open"),
        ("closed", "close"),
        ("cancelled", "cancelled"),
    )

    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    sponsorship_deadline = models.DateField()
    description = models.TextField()
    category = models.CharField(max_length=100)  # Sports, Hackathon
    # Open, Closed, Cancelled
    status = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    organizer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="event_organizer",
        limit_choices_to={"is_organizer": True},
    )

    def __str__(self):
        return self.title


class SponsorshipTier(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="sponsorship_tier"
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    benefits = models.TextField()

    def __str__(self):
        return f"{self.event.title} - {self.name}"


class Sponsorship(models.Model):
    sponsor = models.ForeignKey(
        Account, on_delete=models.CASCADE, limit_choices_to={"is_sponsor": True}
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, limit_choices_to={"status": "open"}
    )
    tier = models.ForeignKey(SponsorshipTier, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (
            "sponsor",
            "event",
            "tier",
        )  # Ensure unique sponsorship per event and tier

    def __str__(self):
        return f"{self.sponsor.username} sponsors {self.event.title} at {self.tier.name} tier"