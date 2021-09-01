from .serializers import PokemonsSerializer,SinglePokemonSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import json
import requests


# PokeList view allows the whole pokemon list to be returned.
class PokeList(APIView):
    def get(self,request):
        poke_list = []
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1118")
        result= json.loads(response.text)
        names = result["results"]
        for i in names:
            poke_list.append(i) # list of pokemons (names,urls)
       
        id = 1 
        for i in range(len(poke_list)): #we add pictures to the pokemon list with the help of a different api
            poke_list[i]["img"] = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{id}.svg"
            id+=1

        results = PokemonsSerializer(poke_list, many=True).data
        return Response(results)


# SinglePoke view ensures that the pokemon whose id is given will return
class SinglePoke(APIView):
    def get(self,request,pk):
        poke_list = []
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pk}")
        
        result= json.loads(response.text)
        pokes = result["forms"]
        abilities = result["abilities"]

        for i in pokes:
            poke_list.append(i)

        for i in range(len(poke_list)):
            poke_list[i]["img"] = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/{pk}.svg"

        #Adding abilities along with the same steps as above
        for i in range(len(abilities)):
            if abilities[i]["is_hidden"]==True:
                get_ability = abilities[i]["ability"]["name"]
                for i in range(len(poke_list)):
                    poke_list[i]["ability"] = get_ability
        
        results = SinglePokemonSerializer(poke_list, many=True).data
        return Response(results)
        
