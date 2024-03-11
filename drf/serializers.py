from rest_framework import serializers
from drf.models import Todo, Currency
from account.models import User


class TodoSerializer(serializers.ModelSerializer):

    def validate_priority(self, priority):
        if priority < 0 or priority > 10:
            raise serializers.ValidationError('Priority must be between 1 and 10')
        return priority

    class Meta:
        model = Todo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'todos']


class CurrecySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'