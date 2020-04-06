import copy
import os
import sys
from texttable import Texttable


import constants

# Create a deep copy of the original file
player_data = copy.deepcopy(constants.PLAYERS)
team_data = copy.deepcopy(constants.TEAMS)


# create a way to clean all teams based on variables instead of 
# doing steps for every team. Trying to keep it DRY and clean

def make_teams(cleaned_players):
    distributed_teams = 0
    for player in cleaned_players:
        teams[team_data[distributed_teams]].append(
            {'name': player['name'],
             'guardians': player['guardians'].split(' and '),
             'experience': True if player['experience'] == 'YES' else False,
             'height': int(player['height'][0:3])
             }
        )
        distributed_teams = (distributed_teams + 1) % len(team_data)



def which_team(select_team):
    if 0 <= select_team < len(team_data):
        return True
    else:
        return False

if __name__ == "__main__":

    # Evenly distribute experienced players and inexperienced players
    teams = {team: [] for team in team_data}
    exp_players = [player for player in player_data if player['experience'] == 'YES']
    inexp_players = [player for player in player_data if player['experience'] == 'NO']
    make_teams(exp_players)
    make_teams(inexp_players)

    # Using a function instead of while True as suggested by @megan from TreeHouse
    start_screen = True
    while start_screen:
        print('--------------------------------------------------')
        print('--------------------------------------------------')

        print(
    '''   BASKETBALL STATS TOOL
            ________ 
    o      |   __   | The choice is yours my friend!'
      \_ O |  |__|  |   1) Show teams stats as table
   ____/ \ |___WW___|   2) Let's me out I'm bored!
   __/   /     ||      
               ||
               ||
_______________||________________________________''')
        print('--------------------------------------------------\n')

        # This is the beginning of the menu prompting user for what to do
        start_screen = input("What would you like? (i.e 1 or 2): ")

        # Clears the screen so that the console looks clean through each step 
        # TODO, implement a catch for windows machines. i.e ('cls')
        os.system('clear')

        try:
            start_screen = int(start_screen)
            if start_screen < 1 or start_screen > 2:
                raise ValueError("Input is out of range")
        except ValueError:
            print("OOPS, YOU DIDN'T ENTER A VALID OPTION!!")
        else:
            if start_screen == 1:

                for i, team in enumerate(team_data, start=1):
                    print("==========> "f'{i}) {team}')

                team_input = input('''Ok, you're a statistics nerd!:\r\nPick your team to get your fill of cool stats!:  ''')
                os.system('clear')
                try:
                    team_input = int(team_input)-1
                    if not which_team(team_input):
                        raise ValueError("Input is out of range")
                except ValueError as err:
                    print("We ran out into an issue : {}".format(err))
                else:
                    team_name = team_data[team_input]
                    # TODO - remove '[]' from being displayed in table
                    player = [player['name'] for player in teams[team_name]]
                    team_guards = ([guardians for player in teams[team_name] for guardians in player['guardians']])
                    num_exp_players = (len([player['name'] for player in teams[team_name] if player['experience']==True]))
                    num_inexp_players = (len([player['name'] for player in teams[team_name] if player['experience']==False]))
                    print(f'\nHere are the stats for: {team_name}')

                    total_players = len(teams[team_name])
                    avg_height = sum(player['height'] for player in teams[team_name])//total_players
                    table = Texttable()
                    table.set_cols_width([30, 30, 10, 11, 8, 8])
                    table.set_cols_align(["l", "l", "l", "l", "l", "l"])
                    table.set_cols_valign(["l", "l", "c", "c", "c", 'c'])
                    table.add_rows([[".  Players Name.  ", "Guardians", "Non-exp\r\nPlayers", "Experienced Players", "Average Player's\r\nheight", "Total number\r\nof players"],
                        [player, team_guards,num_inexp_players ,num_exp_players, {avg_height}, {total_players}]])
                    print(table.draw())
        
            if start_screen == 2:
                sys.exit(0)

                print('''

        Hope you had fun!!! See you next time!!!
                              =_-___
                    o    \__ \ 
                   o       __| \ 
                    o      \__  \ 
                      oooo    \  \ 
                               \  \ 
 __________________             |   \ 
|__________________|             \   |
 \/\/\/\/\/\/\/\/\/     _----_    |   |
  \/\/\/\/\/\/\/\/     |      \   |   |
   \/\/\/\/\/\/\/      |       |    |  |
    |/\/\/\/\/\|        |       \__/    |
    |/\/\/\/\/\|         __---          |
    |/\/\/\/\/\|       /   \            |
                      |     |    23    |
                      |   /            |
                      |   \            |
                      |   | \          |
                      |   |   \____-----\ 
                      |   |    \____-----
                       |  |    |          \ 
                       |  |   |             \ 
                        \  \_|_      |       |
                         \____/  ___/ \_____/\ 
                            /    /       \     \ 
                          /     /          \     \ 
                         /    /              \    \ 
                       /    /                  \    \ 
                      /   /                      \   \ 
                /\   /  /                          \  |
               |  \/ \/                              \/ \ 
                \    |                             __/   |
                  \_/                            /______/''')


    