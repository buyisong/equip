from rest_framework import serializers
from app_login.models import User


class UserSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    phone = serializers.CharField(max_length=11)
    email = serializers.CharField()

    def create(self, validated_data):
        # validated_data 校验通过的数据，就是USER_OBJ
        # 通过orm给Book表增加数据
        user_obj = User.objects.create(username=validated_data["username"], password=validated_data["password"],
                                       phone=validated_data["phone"], email=validated_data["email"])
        print(user_obj)

    def update(self, instance, validated_data):
        # instance 更新的user_obj对象
        # validated_data 校验通过的数据
        # orm的更新
        instance.username = validated_data.get("username", instance.username)
        instance.password = validated_data.get("password", instance.password)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.save()
        return instance
