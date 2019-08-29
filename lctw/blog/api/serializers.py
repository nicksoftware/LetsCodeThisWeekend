from rest_framework import serializers
from blog.models import Post

class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'content',
        ]
