from django.shortcuts import render
from events.models import Event


def index(request):
    events = Event.objects.order_by("-start_date")[:3]
    return render(request, "index.html", {"events": events})
