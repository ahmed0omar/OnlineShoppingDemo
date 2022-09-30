from djoser.serializers  import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer
from rest_framework import serializers
class UserCreateSerializer(BaseUserCreateSerializer):
    id=serializers.UUIDField(read_only=True)
    class Meta(BaseUserCreateSerializer.Meta):
        fields=['id','first_name','last_name','username','email','password']
       
class UserSerializer( BaseUserSerializer):
    
    class Meta(BaseUserSerializer.Meta):
        fields=['id','first_name','last_name','username','email']
        