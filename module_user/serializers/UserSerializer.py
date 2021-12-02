from rest_framework import serializers
from module_user.models.User import User
# from module_general_validators import get_user_password_validations


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            'id', 'first_name', 'last_name', 'username', 'primary_email', 'primary_phone', 'password', 'avatar',
            'status', 'created', 'updated'
        ]
        read_only_fields = ('status', 'created', 'updated')

        # validators = get_user_password_validations('password')
