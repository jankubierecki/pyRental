from rest_framework import serializers

from rentals.models import Rental
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    rentals = serializers.PrimaryKeyRelatedField(many=True, queryset=Rental.objects.all())

    class Meta:
        model = Profile
        fields = ('id', 'user_id', 'rentals',)
