from django_filters import FilterSet, DateFilter

from rooms.models import Room


class RoomFilterSet(FilterSet):
    start_date = DateFilter(
        field_name="reservations__end_date",
        lookup_expr="lte",
    )
    end_date = DateFilter(
        field_name="reservations__start_date",
        lookup_expr="gte",
    )

    class Meta:
        model = Room
        fields = ["start_date", "end_date"]
