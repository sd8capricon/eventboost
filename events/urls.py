from django.urls import path
from events.views import (
    EventsList,
    EventDetailView,
    CreateEvent,
    EventsListOrganizer,
    EditEvent,
    AddSponsorshipTier,
    EditSponsorShipTier,
)

urlpatterns = [
    path("", EventsList.as_view(), name="events"),
    path("<int:pk>/", EventDetailView.as_view(), name="event"),
    path("create_event/", CreateEvent, name="create_event"),
    path("manage_events/", EventsListOrganizer.as_view(), name="manage_events"),
    path("manage_events/<int:pk>/", EditEvent, name="edit_event"),
    path("manage_events/<int:pk>/add_tier", AddSponsorshipTier, name="add_tier"),
    path(
        "manage_events/<int:pk>/edit_tier/<int:tier_pk>",
        EditSponsorShipTier,
        name="edit_tier",
    ),
]
