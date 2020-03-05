from django.urls import path
from lib import apiendpoints
from .views.post.postlistview import PostListView
from .views.post.postdetailview import PostDetailView

urlpatterns = [
	path(apiendpoints.POST_PATH, PostListView.as_view()),
	path(apiendpoints.POST_DETAIL_PATH, PostDetailView.as_view()),
]
