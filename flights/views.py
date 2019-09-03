from rest_framework.generics import (ListAPIView, RetrieveAPIView,
	RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView,
	)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from datetime import datetime

from .models import Flight, Booking
from .serializers import (FlightSerializer, BookingSerializer,
	BookingDetailsSerializer, UpdateBookingSerializer,
	# UserLoginSerializer,
	)


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer


class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = UpdateBookingSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

# class UserLogin(APIView):
# 	serializer_class = UserLoginSerializer

# 	def post(self, request):
# 		my_data = request.data
# 		serializer = UserLoginSerializer(data=my_data)
# 		if serializer.is_valid(raise_exception=True):
# 			valid_data = serializer.data
# 			return Response(valid_data, status=HTTP_200_OK)
# 		return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class CreateBooking(CreateAPIView):
	serializer_class = UpdateBookingSerializer

	def perform_create(self, serializer):
		# lookup_field = 'self.flight.id'
		# lookup_url_kwarg = 'flight_id'
		serializer.save(flight_id=self.kwargs['flight_id'], user=self.request.user)

