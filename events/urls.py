from django.urls import path
from events.views import (
    EventsList,
    EventDetailView,
    CreateEvent,
    EventsListSponsor,
    DeleteEventSponsorship,
    EventsListOrganizer,
    EditEvent,
    DeleteEvent,
    AddSponsorshipTier,
    EditSponsorShipTier,
    DeleteEventTier,
    SponsorEvent,
)

urlpatterns = [
    path("", EventsList.as_view(), name="events"),
    path("<int:pk>/", EventDetailView.as_view(), name="event"),
    path("create_event/", CreateEvent, name="create_event"),
    path(
        "manage_sponsorships/", EventsListSponsor.as_view(), name="manage_sponsorships"
    ),
    path(
        "manage_sponsorships/delete/<int:pk>",
        DeleteEventSponsorship,
        name="delete_sponsorship",
    ),
    path("manage_events/", EventsListOrganizer.as_view(), name="manage_events"),
    path("manage_events/<int:pk>/", EditEvent, name="edit_event"),
    path("manage_events/delete/<int:pk>", DeleteEvent, name="delete_event"),
    path("manage_events/<int:pk>/add_tier", AddSponsorshipTier, name="add_tier"),
    path(
        "manage_events/<int:pk>/edit_tier/<int:tier_pk>",
        EditSponsorShipTier,
        name="edit_tier",
    ),
    path(
        "manage_events/<int:pk>/delete_tier/<int:tier_pk>",
        DeleteEventTier,
        name="delete_tier",
    ),
    path("sponsor/<int:pk>/<int:tier_pk>", SponsorEvent, name="sponsor_event"),
]
