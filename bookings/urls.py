from django.urls import path
from . import views

urlpatterns = [
    path("", views.bookings_home, name="view_bookings"),
    path("create_booking", views.create_booking, name="add_booking"),
    path("edit_booking/<booking_id>", views.edit_booking, name="edit_booking"),
    path("delete_booking/<booking_id>", views.delete_booking, name="delete_booking"),
    path("view_slots", views.view_slots, name="view_slots"),
    path("book_slot/<slot_id>", views.book_slot, name="book_slot"),
    path("view_my_slots", views.view_booked_slots, name="my_bookings"),
    path("cancel/<slot_id>", views.cancel_slot, name="cancel_slot"),
]