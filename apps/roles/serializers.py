from rest_framework import serializers
from apps.roles.models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

    def validate_name(self, value):
        if Role.objects.filter(name=value).exists():
            raise serializers.ValidationError("Role name must be unique.")
        return value

    def validate_level(self, value):
        if not isinstance(value, int) or value <= 0:
            raise serializers.ValidationError("Level must be a positive integer.")
        return value

    def validate_permissions(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("Permissions must be a JSON object.")
        for k, v in value.items():
            if not isinstance(v, bool):
                raise serializers.ValidationError(f"Permission '{k}' must be a boolean.")
        return value
