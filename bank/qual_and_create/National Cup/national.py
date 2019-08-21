import random as r
import os
from colorama import init, Fore, Back, Style


class Player():
    def __init__(self):
        self.name = ""
        self.nation = ""
        self.team = ""
        self.role = ""
        self.farm = 0
        self.fight = 0
        self.teamwork = 0
    def Overall(self):
        ovr = int((self.teamwork + self.fight + self.farm) / 3)
        return ovr

def scan_teams():
    app_path = os.path.dirname(os.path.realpath(__file__))
    dir_list = os.listdir(app_path)
    if 'upgrader.py' in dir_list:
        dir_list.remove('upgrader.py')
    if 'main.py' in dir_list:
        dir_list.remove('main.py')
    if 'national.py' in dir_list:
        dir_list.remove('national.py')
    # if 'National Teams' in dir_list:
    #     dir_list.remove('National Teams')
    return dir_list

def scan_player(path : str):
    f = open(path)
    data = f.readlines()
    f.close()
    p = Player()
    p.name = data[0][:-1]
    p.nation = data[1][:-1].upper()
    p.farm = int(data[2].split()[1])
    p.fight = int(data[3].split()[1])
    p.teamwork = int(data[4].split()[1])
    p.role = data[5].split()[1]
    return p

def write_player(path : str, player : Player):
    f = open(path + "\\" + player.name + '.plr', 'w')
    f.write(player.name + '\n')
    f.write(player.nation + '\n')
    f.write('Farm: ' + str(player.farm) + '\n')
    f.write('Fight: ' + str(player.fight) + '\n')
    f.write('Team_Work: ' + str(player.teamwork) + '\n')
    f.write('Position: ' + player.role)
    f.close()

def main():
    app_path = os.path.dirname(os.path.realpath(__file__))
    players = []

    teams = scan_teams()

    if "National Teams" in teams:
        teams.remove("National Teams")
        if "info" in os.listdir(app_path + "\\" + "National Teams"):
            pass
        else:
            os.mkdir("National Teams" + "\\" + "info")
    else:
        os.mkdir("National Teams")
        os.mkdir("National Teams" + "\\" + "info")

    for team in teams:

        t_players = os.listdir(app_path + "\\" + team)
        print("Team", team, t_players)

        for t_player in t_players:
            t_p = scan_player(app_path + "\\" + team + "\\" + t_player)
            t_p.team = team
            players.append(t_p)
    print(players)

    existing_nations = []
    while len(players) > 0:

        player = players[0]
        if player.nation in existing_nations:
            pass
        else:
            existing_nations.append(player.nation)
            os.mkdir("National Teams" + "\\" + player.nation)
        t_players = []
        t_players.append(player)
        players.remove(player)
        role = player.role
        nation = player.nation
        if nation == "CHI" and role == "Sup":
            i = 1
            pass
        for_remove = []
        for pl in players:
            if pl.nation == nation and pl.role == role:
                t_players.append(pl)
                for_remove.append(pl)
        for player in for_remove:
            players.remove(player)

        if nation == "CHI" and role == "Sup":
            for t_pl in t_players:
                print(t_pl.name, t_pl.team)
            print("\n")


        if len(t_players) == 1:
            write_player("National Teams" + "\\" + nation, t_players[0])
            f = open("National Teams" + "\\" + "info" + "\\" + nation + ".txt", 'a')
            f.write(t_players[0].name + " [" + t_players[0].role + "] (" + t_players[0].team + ") "
                    + str(t_players[0].Overall()) + " only one" + "\n" )
            f.close()
        else:
            max_p = t_players[0]
            t_players.remove(max_p)
            for player in t_players:
                if player.Overall() > max_p.Overall():
                    max_p = player

            write_player("National Teams" + "\\" + nation, max_p)
            f = open("National Teams" + "\\" + "info" + "\\" + nation + ".txt", 'a')
            f.write(max_p.name + " [" + max_p.role + "] (" + max_p.team + ") "
                    + str(max_p.Overall()) + "\n")
            f.close()



main()