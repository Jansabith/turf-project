from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Turf
from .forms import TurfForm

from django.shortcuts import render, get_object_or_404
from .models import Turf
from booking.models import TimeSlot, Booking

@login_required
def create_turf(request):

    if request.user.user_type != "owner":
        return redirect("home")

    if request.method == "POST":

        form = TurfForm(request.POST, request.FILES)

        if form.is_valid():

            turf = form.save(commit=False)
            turf.owner = request.user
            turf.save()

            return redirect("home")

        else:
            print(form.errors)   # 🔴 shows errors in terminal

    else:
        form = TurfForm()

    return render(request, "create_turf.html", {"form": form})


def turf_detail(request, id):

    turf = get_object_or_404(Turf, id=id)

    slots = TimeSlot.objects.filter(turf=turf)

    joined_slots = []

    if request.user.is_authenticated and request.user.user_type == "player":
        joined_slots = Booking.objects.filter(
            player=request.user
        ).values_list("timeslot_id", flat=True)

    return render(request, "turf_detail.html", {
        "turf": turf,
        "slots": slots,
        "joined_slots": joined_slots
    })


@login_required
def delete_slot(request, slot_id):

    slot = get_object_or_404(TimeSlot, id=slot_id)

    # Only turf owner can delete slot
    if request.user == slot.turf.owner:
        slot.delete()

    return redirect("home")


@login_required
def delete_turf(request, turf_id):

    turf = get_object_or_404(Turf, id=turf_id)

    # Only owner can delete
    if request.user == turf.owner:
        turf.delete()

    return redirect("home")


@login_required
def exit_slot(request, slot_id):

    timeslot = get_object_or_404(TimeSlot, id=slot_id)

    booking = Booking.objects.filter(
        player=request.user,
        timeslot=timeslot
    ).first()

    if booking:
        booking.delete()

        # update slot status
        if timeslot.is_full:
            timeslot.is_full = False
            timeslot.save()

    return redirect("home")


@login_required
def edit_turf(request, turf_id):

    turf = get_object_or_404(Turf, id=turf_id)

    if request.user != turf.owner:
        return redirect("home")

    if request.method == "POST":

        form = TurfForm(request.POST, request.FILES, instance=turf)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = TurfForm(instance=turf)

    return render(request, "create_turf.html", {
        "form": form,
        "edit": True
    })

