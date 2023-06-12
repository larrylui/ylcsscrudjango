from rest_framework import serializers
from .models import User, Crush

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['class_no', 'student_no', 'unique_id']

class CrushSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    crush = UserSerializer()

    class Meta:
        model = Crush
        fields = ['user', 'crush', 'matched']