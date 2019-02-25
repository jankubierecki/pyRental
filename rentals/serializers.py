from rest_framework import serializers

from rentals.models import Rental


class RentalSerializer(serializers.ModelSerializer):
    profile = serializers.ReadOnlyField(source='profile.user.username')

    class Meta:
        model = Rental
        fields = ('id', 'car', 'profile', 'start_date', 'end_date', 'paid')
