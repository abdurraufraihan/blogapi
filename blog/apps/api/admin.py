from django.contrib import admin
from apps.user.models import User
from lib import constants as const

class UserAdmin(admin.ModelAdmin):
	list_display = [
		const.USER_NAME_PROPERTY,
		const.EMAIL_PROPERTY
	]

admin.site.register(User, UserAdmin)
