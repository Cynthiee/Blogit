from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class PostSerializer(serializers.ModelSerializer):
    Category = CategorySerializer()
    model = Post
    fields =('id', 'title', 'content', 'created_at', 'updated_at', 'category' )

