from constants import TEAMS, PLAYERS

# Print App Menu
def print_menu():
    print("""

MENU:
-> A: Display Team Stats
-> B: Quit
          """)

# Prompt user for input and return their selection
def prompt_user():
    return input('\n>> Enter an option:  ')

# Clean up the height, experience, and guardian fields
def clean_data(data):
    players = []
    for record in data:
        player = {}
        player['name'] = record['name']
        player['guardians'] = record['guardians'].split(' and ')
        player['experience'] = bool(record['experience'] == 'YES')
        player['height'] = int(record['height'].split(' ').pop(0))
        players.append(player)
    return players    

# Create teams with balanced number of players and balanced player experience
def balance_teams(team_data, player_data):

    # Placeholders to add inexperienced and experiened players to
    experienced_players = []
    inexperienced_players = []

    # Divide players into experienced and inexperienced groups
    for player in player_data:
        if player['experience'] == True:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)

    # Create a new list that will hold team dictionaries
    teams = []
    for record in team_data:
        team = {}
        team['team_name'] = record
        team['players'] = []
        team['guardians'] = []
        teams.append(team)

    # Get the number of experienced players and inexperienced players per team
    experienced_per_team = int(len(experienced_players) / len(teams))
    inexperienced_per_team = int(len(inexperienced_players) / len(teams))

    # Loop through the teams and for each one, loop through the experienced players and inexperienced players based on how many of each group should be on each team, adding the appropriate player and player info to the team
    for team in teams:
        experienced_count = 0
        inexperienced_count  = 0
        total_height = 0
        for i in range(experienced_per_team):
            player = experienced_players.pop()
            team['players'].append(player['name'])
            team['guardians'] = team['guardians'] + player['guardians']
            experienced_count += 1
            total_height += player['height']
        for i in range(inexperienced_per_team):
            player = inexperienced_players.pop()
            team['players'].append(player['name']) 
            team['guardians'] = team['guardians'] + player['guardians']
            inexperienced_count += 1
            total_height += player['height']
        team['experienced_players'] = experienced_count
        team['inexperienced_players'] = inexperienced_count
        team['average_height'] = total_height / len(team['players'])
    return teams

# Print Team List
def print_team_list(teams):
    print("\nTEAMS:\n")
    list_start = 1
    for team in teams:
        print(f"{list_start}: {team['team_name']}")
        list_start += 1

# Draw Blanks to match length of string
def draw_blanks(*args):
    first, second = args
    total_blanks = len(first) + len(second)
    blanks = '-' * total_blanks
    return blanks

# Print Team Stats in readible format
def print_team_stats(team):
    print(f"""

Team: {team['team_name']} Stats
{draw_blanks(team['team_name'], 'Team:  Stats')}
Total Players: {len(team['players'])}
Total Experienced: {team['experienced_players']}
Total Inexperienced: {team['inexperienced_players']}
Average Height: {round(team['average_height'], 2)}"

Roster:
{", ".join(team['players'])}

Guardians:
{", ".join(team['guardians'])}
    """)

# Dunder main condition to ensure the app doesn't auto-run on import
if __name__ == '__main__':
    players = clean_data(PLAYERS)
    teams = balance_teams(TEAMS, players)
    print('\n\n====== Basketball Stats Tool 1.0 ======')

    while True:
        print_menu()
        menu_selection = prompt_user()

        if menu_selection.upper() == 'A':
            print_team_list(teams)

            try:
                team_selection = int(prompt_user())
                if team_selection > len(teams):
                    print('\nInvalid selection.')
                    continue
                else:
                    team_index = team_selection - 1
                    print_team_stats(teams[team_index])
                    input("\nPress 'Enter' to continue...")
            except ValueError:
                print('\nSelection must be a number.')
                continue

        elif menu_selection.upper() == 'B':
            break
        else:
            print('\nInvalid selection.\n')
            continue