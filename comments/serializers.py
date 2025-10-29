from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'parent', 'created_at', 'updated_at']
        read_only_fields = ['author', 'parent', 'created_at', 'updated_at']

    def get_replies(self, obj):
        #this method automatically nests replies under each comment
        replies = obj.replies.all()
        return CommentSerializer(replies, many=True).data