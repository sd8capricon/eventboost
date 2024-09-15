from django.shortcuts import render
from events.models import Event


def index(request):
    events = Event.objects.order_by("pk")[:3]
    return render(request, "index.html", {"events": events})
