from rest_framework.generics import ListCreateAPIView
from taxonomy.models import Tag
from taxonomy.serializer.tagserializer import TagSerializer

class TagListCreateView(ListCreateAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
