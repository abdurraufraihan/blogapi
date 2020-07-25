from django.contrib.auth import password_validation
from rest_framework import serializers
from apps.user.models import User
from lib import constants as const, errormessages as errorMessage

class UserSignupSerializer(serializers.ModelSerializer):
	retypePassword = serializers.CharField()

	class Meta:
		model = User
		fields = [
			const.USER_NAME_PROPERTY,
			const.EMAIL_PROPERTY,
			const.PASSWORD_PROPERTY,
			const.RETYPE_PASSWORD_PROPERTY
		]

	def validate(self, data):
		if data[const.PASSWORD_PROPERTY] != data[const.RETYPE_PASSWORD_PROPERTY]:
			raise serializers.ValidationError(
				{const.ERROR_PROPERTY:
					errorMessage.PASSWORD_DOES_NOT_MATCH_ERROR}
			)
		return data

	def create(self, validatedData):
		validatedData.pop(const.RETYPE_PASSWORD_PROPERTY)
		return User.objects.create(**validatedData)
