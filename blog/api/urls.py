from django.urls import path
from lib import apiendpoints
from .views.post.postlistview import PostListView

urlpatterns = [
	path(apiendpoints.POST_PATH, PostListView.as_view()),
]
