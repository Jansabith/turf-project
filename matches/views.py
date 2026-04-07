from django.shortcuts import render, get_object_or_404
from booking.models import TimeSlot
from .models import Team


def view_teams(request, slot_id):

    slot = get_object_or_404(TimeSlot, id=slot_id)

    team_a = Team.objects.get(timeslot=slot, team_name="Team A")
    team_b = Team.objects.get(timeslot=slot, team_name="Team B")

    return render(request, "teams.html", {
        "slot": slot,
        "team_a": team_a.players.all(),
        "team_b": team_b.players.all(),
    })