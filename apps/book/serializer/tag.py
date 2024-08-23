from rest_framework import serializers
from apps.book.models import Tag


class TagSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name.capitalize()

    def validate_name(self, value):
        if any(char in value for char in '!@#$%^&*'):
            raise serializers.ValidationError('name should not contain special characters')
        return value
    
            # my selution .. try it
         #if attrs.get('__all__') == attrs.get('%','!','@','#','$','%','&','*'):
            #raise serializers.ValidationError('the tag should not contain ...')

    class Meta:
        model = Tag
        fields = '__all__' 
        read_only_field = ('id',) 