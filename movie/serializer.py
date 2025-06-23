from rest_framework import serializers
from .models import User,Language,Movies,Genre,Country,Actor,Industry

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userName', 'email', 'password', 'mobileNo']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # ✅ Secure password hash
        user.save()
        return user

class loginSerializer(serializers.Serializer):
    username = serializers.CharField(label="Username")
    password = serializers.CharField(label="Password", style={'input_type': 'password'}, write_only=True)

class languageSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'  

class genreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'      

class actorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class industrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'
        
class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class MovieReadSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    languages = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    countries = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)
    industries = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'