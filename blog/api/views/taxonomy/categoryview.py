from rest_framework.generics import ListCreateAPIView
from taxonomy.models import Category
from taxonomy.serializer.categoryserializer import CategorySerializer

class CategoryView(ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
