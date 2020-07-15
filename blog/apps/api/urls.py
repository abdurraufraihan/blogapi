from django.urls import path
from lib import apiendpoints
from .views.post.postlistcreateview import PostListCreateView
from .views.post.postretriveupdatedestroyview import \
	PostRetrieveUpdateDestroyView
from .views.taxonomy.categoryview import CategoryListCreateView, \
	CategoryRetrieveUpdateDestroyView
from .views.taxonomy.tagview import TagListCreateView, \
	TagRetrieveUpdateDestroyView
from .views.comment.commentlistcreateview import CommentListCreateView

urlpatterns = [
	path(apiendpoints.POST_URL, PostListCreateView.as_view()),
	path(
		apiendpoints.POST_DETAIL_URL,
		PostRetrieveUpdateDestroyView.as_view()
	),
	path(apiendpoints.COMMENT_URL, CommentListCreateView.as_view()),
	path(apiendpoints.CATEGORY_URL, CategoryListCreateView.as_view()),
	path(
		apiendpoints.CATEGORY_DETAIL_URL,
		CategoryRetrieveUpdateDestroyView.as_view()
	),
	path(apiendpoints.TAG_URL, TagListCreateView.as_view()),
	path(apiendpoints.TAG_DETAIL_URL, TagRetrieveUpdateDestroyView.as_view()),
]
