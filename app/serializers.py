from rest_framework import serializers


class PokemonsSerializer(serializers.Serializer):
   name = serializers.StringRelatedField()
   img = serializers.StringRelatedField()
   # Serializer for list off all the pokemons


class SinglePokemonSerializer(serializers.Serializer):
   name = serializers.StringRelatedField()
   img = serializers.StringRelatedField()
   ability = serializers.StringRelatedField()
   # Serializer for a single pokemon