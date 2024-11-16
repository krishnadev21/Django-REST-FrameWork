from rest_framework import serializers
from .models import Person, Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name']

class PersonSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        color_data = validated_data.pop('color')  # Get color data
        color, created = Color.objects.get_or_create(**color_data)  # Get or create color
        person = Person.objects.create(color=color, **validated_data)  # Create person with color
        return person
    
    def update(self, instance, validated_data):
        # Update color data if provided
        color_data = validated_data.pop('color', None)
        if color_data:
            # Update or create the Color object
            color, created = Color.objects.get_or_create(**color_data)
            instance.color = color  # Set the color for the person

        # Update other fields in the person instance
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)  # Update age if provided
        instance.save()  # Save the instance
        
        return instance

    def validate(self, data):
        special_characters = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        name = data.get('name')
        if name:
            if any(i in special_characters for i in name):
                raise serializers.ValidationError('Name cannot contain special characters.')
        
        age = data.get('age')
        if age is not None and age < 18:
            raise serializers.ValidationError('Age should be greater than 18.')
        
        return data


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    # Another validation method
    # def validate_name(self, value):
    #     special_characters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    #     if any(c in special_characters for c in value):
    #         raise serializers.ValidationError("Name cannot contain special characters")
    #     return value

    # def validate_age(self, value):
    #     if value < 18:
    #         raise serializers.ValidationError("Age should be greater than 18")
    #     return value