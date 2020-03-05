from rest_framework import serializers
from post.models import Post

class PostResponseSerializer(serializers.ModelSerializer):
	def to_representation(self, post):
		responseData = super().to_representation(post)
		if responseData['category']:
			category = responseData.pop('category')
			responseData['category'] = category['name']
		if responseData['tag']:
			tags = responseData.pop('tag')
			responseData['tag'] = [tag['name'] for tag in tags]
		return responseData

	class Meta:
		model = Post
		fields = ['id', 'title', 'description', 'category', 'tag', 'image']
		depth = 1
