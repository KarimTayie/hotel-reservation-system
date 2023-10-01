from django.db.models import Q

from rest_framework import viewsets, mixins, generics, status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from django_filters.rest_framework import DjangoFilterBackend

from rooms.models import Room, Reservation
from rooms.serializers import (
    RoomSerializer,
    ReservationSerializer,
    ReservationCancelSerializer,
)
from rooms.filterSets import RoomFilterSet


class RoomViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [TokenAuthentication]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilterSet
    lookup_field = "room_number"

    def get_queryset(self):
        # Apply filter for is_cancelled=True
        queryset = (
            super()
            .get_queryset()
            .filter(Q(reservations__is_cancelled=True) | Q(reservations__isnull=True))
        )
        return queryset

    def get_permissions(self):
        """Set custom permissions for each action."""
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [AllowAny]
        elif self.action in ["create"]:
            self.permission_classes = [IsAdminUser]

        return super().get_permissions()


class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ReservationCancelView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationCancelSerializer
    lookup_field = "room"

    def perform_update(self, serializer):
        reservation = self.get_object()

        # Check if the authenticated user is the owner of the reservation
        if self.request.user != reservation.user:
            return Response(
                {"error": "You do not have permission to cancel this reservation."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Mark the reservation as cancelled
        serializer.save(is_cancelled=True)
