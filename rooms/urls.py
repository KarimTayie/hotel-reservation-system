from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rooms.views import (
    RoomViewSet,
    ReservationCreateView,
    ReservationCancelView,
)

router = DefaultRouter()
router.register("", RoomViewSet)

app_name = "rooms"

urlpatterns = [
    path(
        "reservations/",
        ReservationCreateView.as_view(),
        name="reservation-create",
    ),
    path(
        "reservations/<int:room>/cancel/",
        ReservationCancelView.as_view(),
        name="reservation-cancel",
    ),
    path("", include(router.urls)),
]
