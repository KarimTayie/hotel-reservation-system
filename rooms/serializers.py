from rest_framework import serializers

from rooms.models import Room, Reservation


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        read_only_fields = ["id"]
        fields = read_only_fields + [
            "room_number",
            "room_type",
            "price_per_night",
        ]


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Reservation
        read_only_fields = ["id"]
        fields = read_only_fields + [
            "start_date",
            "end_date",
            "is_cancelled",
            "room",
            "user",
        ]

    def validate(self, data):
        room = data.get("room")
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        # Check if there are any overlapping reservations for the specified room and date range
        overlapping_reservations = Reservation.objects.filter(
            room=room,
            start_date__lte=end_date,
            end_date__gte=start_date,
            is_cancelled=False,
        ).exclude(pk=self.instance.pk if self.instance else None)

        if overlapping_reservations.exists():
            raise serializers.ValidationError("Room already reserved.")

        return data


class ReservationCancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            "room",
        ]
