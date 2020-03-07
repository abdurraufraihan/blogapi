from rest_framework.permissions import BasePermission
from lib import constants as const

class IsAuthenticatedOrGetRequest(BasePermission):
	def has_permission(self, request, view):
		if request.method == const.REQUEST_METHOD_GET:
			return True
		return request.user and request.user.is_authenticated
