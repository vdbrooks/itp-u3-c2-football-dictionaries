#def players_by_country_and_position(squads_list):
#    pass
import pprint

def convert_player_list_to_dict(player_as_list):
    player_as_dict = {
        'caps': player_as_list[4],
        'club': player_as_list[5],
        'club_country': player_as_list[7],
        'country': player_as_list[6],
        'date_of_birth': player_as_list[3],
        'name': player_as_list[2],
        'number': player_as_list[0],
        'position': player_as_list[1],
        'year': player_as_list[8]
    }
    return player_as_dict  

def players_by_country_and_position(squads_list):
    players = {
        
    }
    
    for player_as_list in squads_list:
        player = convert_player_list_to_dict(player_as_list)
        country = player['country']
        position = player['position']
        
        #if position not in players:
        #    players[position] = []
        #players.setdefault(country, )
        
        if country not in players:
            players[country] = {}
            #players.setdefault(country, {position:[]})
        if position not in players[country]:
            players[country][position] = []
        #   players.setdefault(country, {position:[]})
        
        players[country][position].append(player)
        #list_by_position = players.get(position)
        #list_by_position.append(player)
        #pprint.pprint(players)
    return players


#For reference
"""
def players_by_position(squads_list):
    players = {
    
}

    for player_as_list in squads_list:
        player = convert_player_list_to_dict(player_as_list)
        position = player['position']
        
        #if position not in players:
        #    players[position] = []
        players.setdefault(position,[])
        
        players[position].append(player)
        #list_by_position = players.get(position)
        #list_by_position.append(player)
    return players
"""