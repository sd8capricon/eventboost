from django.db import models
from accounts.models import Account

# Create your models here.


class Event(models.Model):
    CATEGORY_CHOICES = (
        ("conference", "conference"),
        ("workshop", "workshop"),
        ("webinar", "webinar"),
        ("networking", "networking"),
        ("hackathon", "hackathon"),
        ("sports", "sports"),
        ("music", "music"),
        ("art", "art"),
    )

    STATUS_CHOICES = (
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
    # Category Sports, Hackathon
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    # Status Open, Closed, Cancelled
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    expected_attendee_count = models.IntegerField()
    description = models.TextField()
    organizer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="event_organizer",
        limit_choices_to={"is_organizer": True},
    )
    display_picture = models.ImageField(
        null=True, blank=True, upload_to="events/display_picture"
    )
    brochure = models.FileField(null=True, blank=True, upload_to="events/brochure")

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
    date_sponsored = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (
            "sponsor",
            "event",
            "tier",
        )  # Ensure unique sponsorship per event and tier

    def __str__(self):
        return f"{self.sponsor.user.username} sponsors {self.event.title} at {self.tier.name} tier"
