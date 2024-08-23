from rest_framework import serializers
from apps.book.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    #TODO: specify the model that this serializer will link to
    #TODO: specify wich fields should be considerd in the model

    #force django REST to recognize the method
    name = serializers.CharField(read_only=True)
    # Create a serialized method
    username = serializers.SerializerMethodField()
    # Serializerd method's implementation
    def get_username(self, obj): # get <serializer_method_field>
        # obj is the 
        return '_'.join([obj.first_name, obj.last_name])

    def validate_first_name(self,value):  #validate <field_name>
        """Field -level Validation"""

        if '-' in value:
            # Always raise a validation exception
            raise serializers.ValidationError('first mnmae should not contain hyphen (-)')
        
        # if  condition true .. return value
        return value
    
    def validate(self, attrs): # valide
        """Object-Level Validation"""

        if attrs.get('first_name') == attrs.get('last_name'):
            raise serializers.ValidationError('first name and last name should not be the same')
        
        return attrs

    class Meta:
        model = Author
        fields = '__all__' # ('id', 'first_nmae') ... all is to inclode all fields istead to write all 
        read_only_field = ('id',)