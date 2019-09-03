from rest_framework import serializers
# from rest_framework_jwt.settings import api_settings
from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']

# class UserLoginSerializer(serializers.Serializer):
# 	class Meta:
# 		username = serializers.CharField()
# 		password = serializers.CharField(write_only=True)

# 	def validate(self, data):
# 		my_username = data.get('username')
# 		my_password = data.get('password')
# 		try:
# 			user_obj = User.objects.get(username=my_username)
# 		except:
# 			raise serializers.ValidationError("This username does not exist.")
# 		if not user_obj.check_password(my_password):
# 			raise serializers.ValidationError("Incorrect username/password combination")
# 		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# 		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
# 		payload = jwt_payload_handler(user_obj)
# 		token = jwt_encode_handler(payload)
# 		data["token"] = token
# 		return data
