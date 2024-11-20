from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from datetime import datetime, timedelta, time
from django.http import JsonResponse
from .models import BookingSlot
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
def bookings_home(request):
    all_bookings = Booking.objects.filter(owner=request.user)

    context = {
        "bookings": all_bookings,
    }

    return render(request, 'bookings/view_bookings.html', context)


def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking successfully created.")
            return redirect('home')
        else:
            return redirect('view_bookings')
    else:
        form = BookingForm()
        context = {
            "form": form,
        }
        return render(request, 'bookings/create_booking.html', context)

def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking successfully updated.")
            return redirect('home')
        else:
            return redirect('create_booking')
    else:
        form = BookingForm(instance=booking)
        context = {
            "form": form,
        }
        return render(request, 'bookings/edit_booking.html', context)

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking successfully deleted.")
        return redirect("home")
    else:
        return render(request, 'bookings/delete_booking.html')

def view_slots(request):
    slots = BookingSlot.objects.filter(booked=False)
    context = {
        "slots": slots,
    }
    return render(request, 'bookings/make_booking.html', context)

def book_slot(request, slot_id):
    slot = get_object_or_404(BookingSlot, id=slot_id)
    slot.booked = True
    slot.user = request.user
    slot.save()
    return redirect("my_bookings")

def view_booked_slots(request):
    bookings = request.user.bookingslots
    context = {
        "slots": bookings,
    }
    return render(request, 'bookings/view_booked_slots.html', context)

def cancel_slot(request, slot_id):
    slot = get_object_or_404(BookingSlot, id=slot_id)
    slot.booked = False
    slot.user = None
    slot.save()
    return redirect("my_bookings")