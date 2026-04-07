from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import TimeSlot,Booking

from .forms import TimeslotForm,BookingForm
from Turf.models import Turf

from .utils import send_whatsapp

import random

from matches.models import Team


# Owner only can Create slot 

@login_required
def create_slot(request, turf_id):

    turf =get_object_or_404(Turf, id=turf_id)

    if request.user != turf.owner:
        return redirect("home")
    
    if request.method =="POST":

        form=TimeslotForm(request.POST)
        if form.is_valid():
            slot=form.save(commit=False)
            slot.turf=turf
            slot.save()
            return redirect("slot_list",turf_id=turf.id)
    else:
        form=TimeslotForm()

    return render(request,"create_slot.html",{
        "form":form,
        "turf":turf
    })


def slot_list(request, turf_id):

    turf = get_object_or_404(Turf, id=turf_id)
    slots = turf.slots.all()

    return render(request, "slot_list.html", {
        "turf": turf,
        "slots": slots
    })


# PLAYER → JOIN SLOT
# @login_required
# def join_slot(request, slot_id):

#     timeslot = get_object_or_404(TimeSlot, id=slot_id)

#     if request.user.user_type != "player":
#         return redirect("home")

#     if timeslot.is_full:
#         return redirect("home")

#     if request.method == "POST":
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             booking = form.save(commit=False)
#             booking.player = request.user
#             booking.timeslot = timeslot
#             booking.save()

#             timeslot.update_full_status()

#             return redirect("home")
#     else:
#         form = BookingForm()

#     return render(request, "join_slot.html", {
#         "form": form,
#         "timeslot": timeslot
#     })




@login_required
def join_slot(request, slot_id):

    timeslot = get_object_or_404(TimeSlot, id=slot_id)

    # only players allowed
    if request.user.user_type != "player":
        return redirect("home")

    # prevent duplicate join
    if Booking.objects.filter(player=request.user, timeslot=timeslot).exists():
        return redirect("home")

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)
            booking.player = request.user
            booking.timeslot = timeslot
            booking.save()


            # send message to player
            message = f"You joined slot at {timeslot.turf.name} on {timeslot.date} at {timeslot.start_time}"
            send_whatsapp(booking.mobile, message)
               

            # check if slot is full
            if timeslot.current_players() >= timeslot.max_player:
                for b in Booking.objects.filter(timeslot=timeslot):


                    msg = f"Slot is FULL! Match ready at {timeslot.turf.name} Please be on time"
                    send_whatsapp(b.mobile, msg)

                timeslot.is_full = True
                timeslot.save()

                # create teams only once
                if not Team.objects.filter(timeslot=timeslot).exists():

                    bookings = Booking.objects.filter(timeslot=timeslot)

                    players = list(bookings)

                    random.shuffle(players)

                    half = len(players) // 2

                    teamA = Team.objects.create(
                        timeslot=timeslot,
                        team_name="Team A"
                    )

                    teamB = Team.objects.create(
                        timeslot=timeslot,
                        team_name="Team B"
                    )

                    teamA.players.set(players[:half])
                    teamB.players.set(players[half:])

            return redirect("home")

    else:
        form = BookingForm()

    return render(request, "join_slot.html", {
        "form": form,
        "timeslot": timeslot
    })





def view_players(request, slot_id):

    slot = get_object_or_404(TimeSlot, id=slot_id)

    players = slot.bookings.all()

    return render(request, "view_players.html", {
        "slot": slot,
        "players": players
    })


@login_required
def exit_slot(request, slot_id):

    timeslot = get_object_or_404(TimeSlot, id=slot_id)

    booking = Booking.objects.filter(
        player=request.user,
        timeslot=timeslot
    ).first()

    if booking:
        booking.delete()

        # update slot full status
        if timeslot.is_full:
            timeslot.is_full = False
            timeslot.save()

    return redirect("home")


