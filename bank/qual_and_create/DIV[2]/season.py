import random as r
import os
from colorama import init, Fore, Back, Style

def scan_teams():
    app_path = os.path.dirname(os.path.realpath(__file__))
    dir_list = os.listdir(app_path)
    if 'upgrader.py' in dir_list:
        dir_list.remove('upgrader.py')
    if 'main.py' in dir_list:
        dir_list.remove('main.py')
    if 'season.py' in dir_list:
        dir_list.remove('season.py')
    return dir_list

def main():
    inp = input("Add New Tournament/End this Season/Start new season/Add KDA [A/E/S/K]>>")
    if inp == "A":
        tn = input("Tournament name:")
        team1 = input("Winner:")
        team2 = input("Second place:")
        team3 = input("Third place:")
        team4 = input("Fourth place:")

        teams = scan_teams()

        for team in teams:
            if team == team1:
                players = os.listdir(team)
                for player in players:
                    f = open(team + "\\" + player)
                    data =  f.readlines()
                    f.close()
                    data.append("\n" + "||" + tn + "||" + " Winner!" + " - " + team)
                    f = open(team + "\\" + player, 'w')
                    f.writelines(data)
                    f.close()
            if team == team2:
                players = os.listdir(team)
                for player in players:
                    f = open(team + "\\" + player)
                    data =  f.readlines()
                    f.close()
                    data.append("\n" + "||" + tn + "||" + " Second place!" + " - " + team)
                    f = open(team + "\\" + player, 'w')
                    f.writelines(data)
                    f.close()
            if team == team3:
                players = os.listdir(team)
                for player in players:
                    f = open(team + "\\" + player )
                    data =  f.readlines()
                    f.close()
                    data.append("\n" + "||" + tn + "||" + " Third place!" + " - " + team)
                    f = open(team + "\\" + player, 'w')
                    f.writelines(data)
                    f.close()
            if team == team4:
                players = os.listdir(team)
                for player in players:
                    f = open(team + "\\" + player )
                    data =  f.readlines()
                    f.close()
                    data.append("\n" + "||" + tn + "||" + " Fourth place!" + " - " + team)
                    f = open(team + "\\" + player, 'w')
                    f.writelines(data)
                    f.close()
    if inp == "S":
        sn = input("Season name>>")
        for team in scan_teams():
            players = os.listdir(team)
            for player in players:
                f = open(team + "\\" + player)
                data = f.readlines()
                f.close()
                data.append("\n"*2 + "="*10 + sn + "="*10)
                f = open(team + "\\" + player, 'w')
                f.writelines(data)
                f.close()
    if inp == "K":
        for team in scan_teams():
            players = os.listdir(team)
            for player in players:
                f = open(team + "\\" + player)
                data = f.readlines()
                f.close()
                data.append("\n" + "0 0")
                f = open(team + "\\" + player, 'w')
                f.writelines(data)
                f.close()
    if inp == "E":
        for team in scan_teams():
            players = os.listdir(team)
            for player in players:
                f = open(team + "\\" + player)
                data = f.readlines()
                f.close()
                end_str = "\n"
                end_str += 10*"=" + "KDA: " + str(round(float(data[6].split()[0])/float(data[6].split()[1]), 2)) + " " + team + " " + 10*"="
                data.append(end_str)
                data[6] ="0 0" + "\n"
                f = open(team + "\\" + player, 'w')
                f.writelines(data)
                f.close()
main()