from django.urls import path
from .views.post.postlistview import PostListView

urlpatterns = [
	path('posts', PostListView.as_view()),
]
