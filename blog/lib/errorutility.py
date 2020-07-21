from rest_framework import status
from rest_framework.response import Response
from lib import constants as const
from lib import errormessages as errorMessage

def getDoesNotExistError(errorMsg):
	return Response(
		{const.ERROR_PROPERTY : errorMsg},
		status=status.HTTP_404_NOT_FOUND
	)

def getInternalServerError():
	return Response(
		{const.ERROR_PROPERTY : errorMessage.INTERNAL_SERVER_ERROR},
		status=status.HTTP_500_INTERNAL_SERVER_ERROR
	)
