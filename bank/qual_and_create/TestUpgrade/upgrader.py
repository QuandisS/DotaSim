import random as r
import os
from colorama import init, Fore, Back, Style

class Player():
    def __init__(self):
        self.name = ""
        self.farm = 0
        self.fight = 0
        self.teamwork = 0

def scan_teams():
    app_path = os.path.dirname(os.path.realpath(__file__))
    dir_list = os.listdir(app_path)
    if 'upgrader.py' in dir_list:
        dir_list.remove('upgrader.py')
    return dir_list

def scan_player(path : str):
    f = open(path)
    data = f.readlines()
    f.close()
    p = Player()
    p.name = data[0]
    p.farm = int(data[2].split()[1])
    p.fight = int(data[3].split()[1])
    p.teamwork = int(data[4].split()[1])
    return p

def rewrite_player(team : str, player : Player):
    filename = team + "\\" + player.name[:-1] + '.plr'
    f = open(filename, 'r')
    data = f.readlines()
    f.close()

    data[2] = "Farm: " + str(player.farm) + '\n'
    data[3] = "Fight: " + str(player.fight) + '\n'
    data[4] = "Team_Work: " + str(player.teamwork) + '\n'

    f = open(filename, 'w')
    f.writelines(data)
    f.close()

def overall(player : Player):
    ovr = int((player.teamwork + player.fight + player.farm) / 3)
    return ovr

def team_overall(team_name : str):
    players = os.listdir(team_name)
    sum = 0
    for pl in players:
        player = scan_player(team_name + "\\" + pl)
        sum += overall(player)
    return int(sum/5)

def main():
    teams = scan_teams()
    players_ids = []
    up_ids = []
    count = len(teams)
    for i in range(len(teams)*5):
        players_ids.append(i)
    print("All IDs: ", players_ids)
    for i in range(count):
        num = r.randint(0, len(players_ids)-1)
        up_ids.append(players_ids[num])
        players_ids.pop(num)
    print("IDs for upgrade: ", up_ids)
    print("Upgrading..." + '\n'*2)

    pre_teams_ovr = []
    for team in teams:
        pre_teams_ovr.append(team_overall(team))

    console_output = ""
    for i in up_ids:
        team_id = i // 5
        player_id = i % 5
        player_name = os.listdir(teams[team_id])[player_id]
        player = scan_player(teams[team_id] + '\\' + player_name)
        print(player.name[:-1] + " [" + teams[team_id] + "]")

        pre_ovr = overall(player)

        farm_mod = r.randint(-20, 20)
        fight_mod = r.randint(-20, 20)
        teamwork_mod = r.randint(-20, 20)

        if (player.farm + farm_mod) >=20 and (player.farm + farm_mod) <=100:
            player.farm += farm_mod
        if (player.fight + fight_mod) >=20 and (player.fight + fight_mod) <=100:
            player.fight += fight_mod
        if (player.teamwork + teamwork_mod) >=20 and (player.teamwork + teamwork_mod) <=100:
            player.teamwork += teamwork_mod

        past_ovr = overall(player)
        dif = past_ovr-pre_ovr
        if dif > 0:
            print(pre_ovr, '-->', past_ovr, Fore.GREEN + "(" + str(dif) + ")" + Style.RESET_ALL + '\n')
        elif dif == 0:
            print(pre_ovr, '-->', past_ovr, "(" + str(dif) + ")" + '\n')
        else:
            print(pre_ovr, '-->', past_ovr, Fore.RED + "(" + str(dif) + ")" + Style.RESET_ALL + '\n')

        rewrite_player(teams[team_id], player)

    print('\n'*2)
    post_teams_ovr = []
    for team in teams:
        post_teams_ovr.append(team_overall(team))

    for i in range(len(teams)):
        dif = post_teams_ovr[i] - pre_teams_ovr[i]
        if dif > 0:
            print(teams[i], pre_teams_ovr[i], '-->', post_teams_ovr[i], Fore.GREEN + "(" + str(dif) + ")"
                  + Style.RESET_ALL + '\n')
        elif dif == 0:
            print(teams[i], pre_teams_ovr[i], '-->', post_teams_ovr[i], "(" + str(dif) + ")" + '\n')
        else:
            print(teams[i], pre_teams_ovr[i], '-->', post_teams_ovr[i], Fore.RED + "(" + str(dif) + ")"
                  + Style.RESET_ALL + '\n')
main()