from django.shortcuts import render, redirect
from Turf.models import Turf
from datetime import datetime
from booking.models import TimeSlot,Booking
from django.views.decorators.cache import never_cache

@never_cache
def first_home(request):

    turf_count = Turf.objects.count()

    player_count = Booking.objects.count()

    match_count = TimeSlot.objects.filter(is_full=True).count()

    city_count = Turf.objects.values("location").distinct().count()

    return render(request, "first_home.html", {
        "turf_count": turf_count,
        "player_count": player_count,
        "match_count": match_count,
        "city_count": city_count,
    })


def home(request):

    # delete expired slots
    now = datetime.now()

    expired_slots = TimeSlot.objects.filter(
        date__lt=now.date()
    )

    expired_slots.delete()

    # search
    query = request.GET.get("q")

    if query:
        query = query.strip()
        turfs = Turf.objects.filter(location__icontains=query)
    else:
        turfs = Turf.objects.all()

    # find slots already joined by player
    joined_slots = []

    if request.user.is_authenticated and request.user.user_type == "player":
        joined_slots = Booking.objects.filter(
            player=request.user
        ).values_list("timeslot_id", flat=True)

    return render(request, "home.html", {
        "turfs": turfs,
        "query": query,
        "joined_slots": joined_slots
    })