from django.urls import path
from lib import apiendpoints
from .views.post.postlistcreateview import PostListCreateView
from .views.post.postretriveupdatedestroyview import \
	PostRetrieveUpdateDestroyView
from .views.taxonomy.categoryview import CategoryListCreateView, \
	CategoryRetrieveUpdateDestroyView
from .views.taxonomy.tagview import TagListCreateView, \
	TagRetrieveUpdateDestroyView

urlpatterns = [
	path(apiendpoints.POST_PATH, PostListCreateView.as_view()),
	path(
		apiendpoints.POST_DETAIL_PATH,
		PostRetrieveUpdateDestroyView.as_view()
	),
	path(apiendpoints.CATEGORY_PATH, CategoryListCreateView.as_view()),
	path(
		apiendpoints.CATEGORY_DETAIL_PATH,
		CategoryRetrieveUpdateDestroyView.as_view()
	),
	path(apiendpoints.TAG_PATH, TagListCreateView.as_view()),
	path(apiendpoints.TAG_DETAIL_PATH, TagRetrieveUpdateDestroyView.as_view()),
]
