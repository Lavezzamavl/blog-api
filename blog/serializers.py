from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Post, Comment

class RegisterSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only = True, min_length =6)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'body', 'created_at']
        read_only_fields = ['author', 'created_at']
        
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    
    category = CategorySerializer(read_only=True)
    
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False
    )
    
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'author',
            'category', 'category_id', 'status',
            'created_at', 'updated_at', 'comments'
        ]
        read_only_fields = ['slug', 'author', 'created_at', 'updated_at']