from rest_framework.generics import ListCreateAPIView, \
	RetrieveUpdateDestroyAPIView
from taxonomy.models import Category
from taxonomy.serializer.categoryserializer import CategorySerializer

class CategoryListCreateView(ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
