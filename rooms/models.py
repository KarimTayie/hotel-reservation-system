from django.db import models
from django.contrib.auth import get_user_model


from rooms.enums import RoomType


class Room(models.Model):
    room_number = models.IntegerField(unique=True)
    room_type = models.CharField(max_length=10, choices=RoomType.choices)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)


class Reservation(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    is_cancelled = models.BooleanField(default=False)

    # relations
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="reservations",
        to_field="room_number",
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reservations",
    )
