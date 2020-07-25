from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from lib import constants as const
from apps.user.serializer.usersignupserializer import UserSignupSerializer

class SignupUser(APIView):
	def post(self, request, format=None):
		serializer = UserSignupSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			token = Token.objects.create(user=user)
			return Response(
				{const.TOKEN_PROPERTY: token.key}, status=status.HTTP_200_OK
			)
		return Response(
			serializer.errors, status=status.HTTP_400_BAD_REQUEST
		)
