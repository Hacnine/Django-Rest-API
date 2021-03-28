from rest_framework import serializers
from model_serializer.models import Student


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)

    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be start with R')

    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        # fields = '__all__'

        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name': {'read_only': True}}

        # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Field level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'yasin' and ct.lower() != 'khulna':
            raise serializers.ValidationError('City must be Khulna')
        return data








# from rest_framework import serializers
# from validation.models import Student
#
#
# def start_with_r(value):
#     if value[0].lower() != 'r':
#         raise serializers.ValidationError('Name should be start with R')
#
#
# def start_with_k(value):
#     if value[0].lower() != 'k':
#         raise serializers.ValidationError('City name should be start with K')
#
#
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[start_with_r, start_with_k])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         print(instance.name)
#
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
#
# # Field level validation
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full')
#         return value
#
# # Field level validation
#     def validate(self, data):
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'yasin' and ct.lower() != 'khulna':
#             raise serializers.ValidationError('City must be Khulna')
#         return data
#


