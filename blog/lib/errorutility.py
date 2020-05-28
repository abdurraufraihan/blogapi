from rest_framework import status
from rest_framework.response import Response
from lib import constants as const
from lib import errormessages as errorMessage

def getPostDoesNotExistError():
	return Response(
		{const.ERROR_PROPERTY : errorMessage.POST_DOES_NOT_EXIST_ERROR},
		status=status.HTTP_404_NOT_FOUND
	)

def getInternalServerError():
	return Response(
		{const.ERROR_PROPERTY : errorMessage.INTERNAL_SERVER_ERROR},
		status=status.HTTP_500_INTERNAL_SERVER_ERROR
	)
