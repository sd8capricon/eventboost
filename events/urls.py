from django.urls import path
from django.contrib.auth.decorators import login_required
from events import views

urlpatterns = [
    path("", views.EventsList.as_view(), name="events"),
    path("manage_events/", views.EventsListOrganizer.as_view(), name="manage_events"),
    path("create_event/", view=views.CreateEvent, name="create_event"),
    path("manage_events/<int:pk>/", views.EditEvent, name="edit_event"),
    path("manage_events/<int:pk>/add_tier", views.AddSponsorshipTier, name="add_tier"),
    path(
        "manage_events/<int:pk>/edit_tier/<int:tier_pk>",
        views.EditSponsorShipTier,
        name="edit_tier",
    ),
]
