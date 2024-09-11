from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from events.models import Event, SponsorshipTier, Sponsorship
from events.forms import EventForm, TierForm, SponsorshipForm

# Create your views here.


# All Open Events
class EventsList(ListView):
    model = Event
    template_name = "events/events_all.html"
    context_object_name = "events"

    def get_queryset(self):
        events = super().get_queryset().filter(status="open")
        return events


# View All Events for organizer
class EventsListOrganizer(LoginRequiredMixin, ListView):
    model = Event
    template_name = "events/events_table.html"
    context_object_name = "events"

    def dispatch(self, request, *args, **kwargs):
        if request.user.account.is_sponsor:
            return redirect("events")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        organizer = self.request.user.account
        events = super().get_queryset().filter(organizer=organizer)
        return events


# View Single Event in detail
class EventDetailView(DetailView):
    model = Event
    template_name = "events/event_detail.html"
    context_object_name = "event"


# List all Sponsored Events
class EventsListSponsor(LoginRequiredMixin, ListView):
    model = Sponsorship
    template_name = "events/events_sponsorships.html"
    context_object_name = "sponsorships"

    def dispatch(self, request, *args, **kwargs):
        if request.user.account.is_organizer:
            return redirect("events")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        sponsor = self.request.user.account
        sponsorships = super().get_queryset().filter(sponsor=sponsor)
        return sponsorships


# Create Event
@login_required
def CreateEvent(request):
    if not request.user.account.is_organizer:
        return redirect("events")
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(organizer_id=request.user.account.id)
            return redirect("add_tier", pk=event.id)
    else:
        form = EventForm()
    return render(request, "events/event_create.html", {"form": form})


# Edit Event
@login_required
def EditEvent(request, pk):
    event = Event.objects.prefetch_related("sponsorship_tier").get(id=pk)
    if event.organizer != request.user.account:
        return render(request, "access_denied.html")
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect("manage_events")
    else:
        form = EventForm(instance=event)
    return render(request, "events/event_edit.html", {"form": form, "event": event})


# Delete an Event
@login_required
def DeleteEvent(request, pk):
    event = Event.objects.get(id=pk)
    if event.organizer != request.user.account:
        return render(request, "access_denied.html")
    event.delete()
    return redirect("manage_events")


# Add Sponsorship Tier to Event
@login_required
def AddSponsorshipTier(request, pk):
    event = Event.objects.get(id=pk)
    if event.organizer != request.user.account:
        return render(request, "access_denied.html")
    if request.method == "POST":
        form = TierForm(request.POST)
        if form.is_valid():
            form.save(event_id=pk)
            return redirect("edit_event", pk=pk)
    else:
        form = TierForm()
    return render(request, "events/tier_add.html", {"form": form, "event": event})


# Edit Sponsorship Tier of an Event
@login_required
def EditSponsorShipTier(request, pk, tier_pk):
    tier = SponsorshipTier.objects.get(id=tier_pk)
    if tier.event.organizer != request.user.account:
        return render(request, "access_denied.html")
    if request.method == "POST":
        form = TierForm(request.POST, instance=tier)
        if form.is_valid():
            form.save()
            return redirect("edit_event", pk=pk)
    else:
        form = TierForm(instance=tier)
    return render(request, "events/tier_edit.html", {"form": form, "tier": tier})


@login_required
def DeleteEventTier(request, pk, tier_pk):
    tier = SponsorshipTier.objects.get(id=tier_pk)
    if tier.event.organizer != request.user.account:
        return render(request, "access_denied.html")
    tier.delete()
    return redirect("edit_event", pk=pk)


# Sponsor an event tier
@login_required
def SponsorEvent(request, pk, tier_pk):
    if request.user.account.is_organizer:
        return render("access_denied.html")
    if request.method == "POST":
        form = SponsorshipForm(request.POST, event_id=pk, tier_pk=tier_pk)
        if form.is_valid():
            form.save(spon_id=request.user.account.id)
            return redirect("manage_sponsorships")
    else:
        form = SponsorshipForm(event_id=pk, tier_pk=tier_pk)
    return render(request, "events/event_checkout.html", {"form": form})


# Delete a sponsorship
@login_required
def DeleteEventSponsorship(request, pk):
    sponsorship = Sponsorship.objects.get(id=pk)
    if sponsorship.sponsor != request.user.account:
        return render(request, "access_denied.html")
    sponsorship.delete()
    return redirect("manage_sponsorships")
