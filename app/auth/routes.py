from flask import Blueprint, render_template, request
from app.auth.forms import PokemonSummons
import requests

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/your_pokemon', methods=['GET', 'POST'])
def form():
    pokeform = PokemonSummons()
    if request.method == 'POST':
        if pokeform.validate():
            pokename = pokeform.pokename.data
            usable_pokename = str(pokename)
            # api code below

            ditto = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
            pikachu = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
            snorlax = requests.get('https://pokeapi.co/api/v2/pokemon/snorlax')
            garchomp = requests.get('https://pokeapi.co/api/v2/pokemon/garchomp')
            squirtle = requests.get('https://pokeapi.co/api/v2/pokemon/squirtle')
            charizard = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')

            # Below is the dictionary I will loop through in my fuction for each pokemon only using the values of the dictionary to do so:

            working_dict = {
                'ditto' : ditto.json(),
                'pikachu' : pikachu.json(),
                'snorlax' : snorlax.json(),
                'garchomp' : garchomp.json(),
                'squirtle' : squirtle.json(),
                'charizard' : charizard.json()
            }

            def pokemon_attributes(your_dict):
                if usable_pokename.lower() == 'ditto':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[0]
                elif usable_pokename.lower() == 'pikachu':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[1]
                elif usable_pokename.lower() == 'snorlax':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[2]
                elif usable_pokename.lower() == 'garchomp':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[3]
                elif usable_pokename.lower() == 'squirtle':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[4]
                elif usable_pokename.lower() == 'charizard':
                    final_display = []
                    for value in your_dict.values():
                        pokemon_dict = {}
                        pokemon_name = value['forms'][0]['name']
                        pokemon_dict[pokemon_name] = {
                            'Ability' : value['abilities'][0]['ability']['name'],
                            'Base_experience' : value['base_experience'],
                            'Sprite' : value['sprites']['front_shiny'],
                            'Attack base_stat' : value['stats'][1]['base_stat'],
                            'hp base_stat' : value['stats'][0]['base_stat'],
                            'Defense base_stat': value['stats'][2]['base_stat']
                        }
                        final_display.append(pokemon_dict)
                    return final_display[5]
                else:
                    return 'The pokemon you summoned is not yet available. Please refresh the page and try again.'

            return pokemon_attributes(working_dict)
            # api code end   
    return render_template('your_pokemon.html', pokeform=pokeform)