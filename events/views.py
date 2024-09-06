from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from events.models import Event, SponsorshipTier
from events.forms import EventForm, TierForm

# Create your views here.


# All Open Events
class EventsList(ListView):
    model = Event
    template_name = "events/all_events.html"
    context_object_name = "events"

    def get_queryset(self):
        events = super().get_queryset().filter(status="open")
        return events


# View All Events for organizer
class EventsListOrganizer(ListView):
    model = Event
    template_name = "events/events_table.html"
    context_object_name = "events"

    def get_queryset(self):
        organizer = self.request.user.account
        events = super().get_queryset().filter(organizer=organizer)
        return events


# Create Event
def CreateEvent(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(organizer_id=request.user.account.id)
            return redirect("add_tier", pk=event.id)
        # return redirect("manage_events")
    else:
        form = EventForm()
    return render(request, "events/event_create.html", {"form": form})


# Edit Event
def EditEvent(request, pk):
    event = Event.objects.prefetch_related("sponsorship_tier").get(id=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
    else:
        form = EventForm(instance=event)
    return render(request, "events/event_edit.html", {"form": form, "event": event})


# Add Sponsorship Tier to Event
def AddSponsorshipTier(request, pk):
    if request.method == "POST":
        form = TierForm(request.POST)
        if form.is_valid():
            form.save(event_id=pk)
            return redirect("edit_event", pk=pk)
    else:
        form = TierForm()
    return render(request, "events/tier_add.html", {"form": form})


# Edit Sponsorship Tier of an Event
def EditSponsorShipTier(request, pk, tier_pk):
    tier = SponsorshipTier.objects.get(id=tier_pk)
    if request.method == "POST":
        print("got it")
        form = TierForm(request.POST, instance=tier)
        if form.is_valid():
            form.save()
        return redirect("edit_event", pk=pk)
    else:
        form = TierForm(instance=tier)
    return render(request, "events/tier_edit.html", {"form": form, "tier": tier})
