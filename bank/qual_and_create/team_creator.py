import random, os

team_all_points = 0
positions = ["Carry", "Mid", "Offlane", "Semi-Sup", "Sup"]

def write_player(team_name : str, nick : str, position: str, country : str):
    f = open(team_name + "\\" + nick + '.plr', 'w')
    f.write(nick + '\n')
    f.write(country + '\n')
    farm = random.randint(0, 100)
    fight = random.randint(0, 100)
    team_work = random.randint(0, 100)
    global team_all_points
    team_all_points += farm + fight + team_work
    f.write('Farm: ' + str(farm) + '\n')
    f.write('Fight: ' + str(fight) + '\n')
    f.write('Team_Work: ' + str(team_work) + '\n')
    f.write('Position: ' + position)
    f.close()

team_name = input("Team name: ")
os.mkdir(team_name)
nicks = input("Nicks: ").split()
nations = input("Nations: ").split()
for i in range(5):
    j = random.randint(0, len(nations)-1)
    nation = nations[j]
    write_player(team_name, nicks[i], positions[i], nation)
print("Team overall: " + str(int(team_all_points/15)))