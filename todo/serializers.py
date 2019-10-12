from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.Serializer):
    title=serializers.CharField(required=True)
    description=serializers.CharField()
    status=serializers.CharField()
    #created_at = serializers.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title', instance.title)
        instance.decription = validated_data.get('decription', instance.decription)
        instance.status = validated_data.get('status', instance.status)
        #instance.create_at = validated_data.get('create_at', instance.create_at)
        instance.save()
        return instance
