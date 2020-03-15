import os, time, random
from PyQt5 import QtWidgets, QtGui
from forms import test
import sys
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap
from colorama import init, Fore, Back, Style


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = test.Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        #self.ui.pushButton.clicked.connect(self.MyFunction)

        self.ui.scan.clicked.connect(self.scanning)

        #Выбор команд
        a = self.ui.Team1_listWidget.selectedItems()
        b = self.ui.Team2_listWidget.selectedItems()
        print(a)
        print(b)
        ###

        self.ui.version.setText('V. 0.1.4b12-wui')

        self.ui.registr.clicked.connect(self.set_first_team)

        self.ui.players_init.clicked.connect(self.initialize_players)

    def scanning(self):

        self.ui.Team1_listWidget.clear()
        self.ui.Team2_listWidget.clear()

        appPath = os.path.dirname(os.path.realpath(__file__))
        dir_list = os.listdir(appPath)
        print(dir_list)
        self.ui.Team1_listWidget.addItems(dir_list)
        self.ui.Team2_listWidget.addItems(dir_list)

        #msgbox = UI_Dialog()
        #msgbox.show_msg_box('Сканированно!', 'SCAN')


    # Регистрация команд #

    def set_first_team(self):
        self.set_second_team()
        first_team = self.ui.Team1_listWidget.selectedItems()[0].text()
        print('f_team:', first_team)

        #если это файл программы!#
        if first_team == 'main.py':
            msgbox = UI_Dialog()
            msgbox.show_msg_box('Файл программы не может быть командой!', 'DotaSim')
            first_team = ''
            print('f_team:', first_team)
        else:
            self.ui.team1_lineEdit.setText(first_team)
    def set_second_team(self):
        second_team = self.ui.Team2_listWidget.selectedItems()[0].text()
        print('s_team:', second_team)

        #если это файл программы!#
        if second_team == 'main.py':
            msgbox = UI_Dialog()
            msgbox.show_msg_box('Файл программы не может быть командой!', 'DotaSim')
            second_team = ''
            print('s_team:', second_team)
        else:
            self.ui.team2_lineEdit.setText(second_team)

    def initialize_players(self):
        appPath = os.path.dirname(os.path.realpath(__file__))
        print(appPath)

        team_1_name = myapp.ui.team1_lineEdit.text()
        team_2_name = myapp.ui.team2_lineEdit.text()

        team_1_path = appPath + '\\' + team_1_name
        team_2_path = appPath + "\\" + team_2_name

        print(team_1_path)
        print(team_2_path)

        team_1_pl_list = os.listdir(team_1_path)
        team_2_pl_list = os.listdir(team_2_path)

        print(team_1_pl_list)
        print(team_2_pl_list)

        # Генерация первой команды #

        team_1 = {}

        for player_name in team_1_pl_list:
            if player_name.split('.')[1] == 'png':


                print('logo_image_name=', player_name)
                print('team_path=', team_1_path)
                pixmap_path = team_1_path + '\\' + player_name
                pixmap = QPixmap(pixmap_path)
                print('pixmap_path=', pixmap_path)
                #self.ui.t1_logo_label.setPixmap(pixmap)
                #self.ui.t1_logo_label.show()

            else:
                p = Player()
                player_name = player_name.split('.')[0]

                # Открытие файла #

                f = open(team_1_path + '\\' + player_name + '.plr')
                pl_info = f.readlines()
                f.close()
                print(player_name + ' __info:' + str(pl_info))

                p.name = player_name
                p.farm = int(pl_info[2].split(' ')[1])
                p.fight = int(pl_info[3].split(' ')[1])
                p.teamwork = int(pl_info[4].split(' ')[1])
                p.position = pl_info[5].split(' ')[1]
                print(p.farm, p.fight, p.teamwork, p.position)

                team_1[player_name] = p

        print(team_1)

        # Генерация второй команды #

        team_2 = {}

        for player_name in team_2_pl_list:
            if player_name.split('.')[1] == 'png':

                print('logo_image_name=', player_name)
                print('team_path=', team_2_path)
                pixmap_path = team_2_path + '\\' + player_name
                pixmap = QPixmap(pixmap_path)
                print('pixmap_path=', pixmap_path)
                #self.ui.t2_logo_label.setPixmap(pixmap)
                #self.ui.t2_logo_label.show()


            else:
                p = Player()
                player_name = player_name.split('.')[0]

                # Открытие файла #

                f = open(team_2_path + '\\' + player_name + '.plr')
                pl_info = f.readlines()
                f.close()
                print(player_name + ' __info:' + str(pl_info))

                p.name = player_name
                p.farm = int(pl_info[2].split(' ')[1])
                p.fight = int(pl_info[3].split(' ')[1])
                p.teamwork = int(pl_info[4].split(' ')[1])
                p.position = pl_info[5].split(' ')[1]
                print(p.farm, p.fight, p.teamwork, p.position)

                team_2[player_name] = p

        print(team_2)

        a = [team_1, team_2]

        # do_game(a)

        self.game = DoGame(a)
        self.game.start()



class UI_Dialog(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()

    def show_msg_box(self, message, title):
        msg = QtWidgets.QMessageBox
        msg.setIcon(self, QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle(self, title)
        msg.setText(self, message)
        msg.setStandardButtons(self, QtWidgets.QMessageBox.Ok)
        msg.exec_(self)

class Player():
    def __init__(self):
        self.alive = True
        self.farm = 0
        self.fight = 0
        self.teamwork = 0
        self.kills = 0
        self.deaths = 0
        self.assists = 0
        self.deathtimer = 0
        self.position = ''
        self.name = ''
        self.gold = 0
        self.kda = 0



class DoGame(QThread):

    def __init__(self, teams):
        QThread.__init__(self)
        DoGame.team = teams

    def __del__(self):
        self.wait()

    def run(self):

        do_game(self.team)

def do_game(teams):
    team_1 = teams[0]
    team_2 = teams[1]

    print(team_1.keys())
    print(list(team_1.keys())[0])


    # myapp.ui.t1_pl1.setText(list(team_1.keys())[0])
    # myapp.ui.t1_pl2.setText(list(team_1.keys())[1])
    # myapp.ui.t1_pl3.setText(list(team_1.keys())[2])
    # myapp.ui.t1_pl4.setText(list(team_1.keys())[3])
    # myapp.ui.t1_pl5.setText(list(team_1.keys())[4])
    #
    # myapp.ui.t2_pl1.setText(list(team_2.keys())[0])
    # myapp.ui.t2_pl2.setText(list(team_2.keys())[1])
    # myapp.ui.t2_pl3.setText(list(team_2.keys())[2])
    # myapp.ui.t2_pl4.setText(list(team_2.keys())[3])
    # myapp.ui.t2_pl5.setText(list(team_2.keys())[4])


    clock = 0
    sec = 0
    game = True

    def event():
        events = ['farm', 'fight']
        i_n = random.randint(0, 400)
        ev = ''
        if i_n <= 1:
            ev = 'fight'
        else:
            ev = 'farm'
        return ev

    team1_net = 0
    team2_net = 0

    team1_hp = 20000
    team2_hp = 20000

    t1_kills = 0
    t2_kills = 0

    while team1_hp > 0 and team2_hp > 0:



        ev = event()
        #print(ev)
        #print(sec)
        sec += 1
        time.sleep(0.005)
        myapp.ui.Time.display((sec//60))

        if ev == 'farm':
            for player in list(team_1.keys()):
                #print(team_1[player].gold)
                prirost = ((team_1[player].farm * 0.05) + random.uniform(0, 5.9))
                team_1[player].gold += prirost
                #team1_net += prirost
                #print(player + ': ' + str(team_1[player].gold))

            #print('SECOND TEAM::::::')

            for player in list(team_2.keys()):
                #print(team_2[player].gold)
                prirost = ((team_2[player].farm * 0.05) + random.uniform(0, 5.9))
                team_2[player].gold += prirost
                #team2_net += prirost
                #print(player + ': ' + str(team_2[player].gold))

            #set gold

            # myapp.ui.gold_1.setText(str(int(team_1[myapp.ui.t1_pl1.text()].gold)))
            # myapp.ui.gold_2.setText(str(int(team_1[myapp.ui.t1_pl2.text()].gold)))
            # myapp.ui.gold_3.setText(str(int(team_1[myapp.ui.t1_pl3.text()].gold)))
            # myapp.ui.gold_4.setText(str(int(team_1[myapp.ui.t1_pl4.text()].gold)))
            # myapp.ui.gold_5.setText(str(int(team_1[myapp.ui.t1_pl5.text()].gold)))
            #
            # myapp.ui.gold_6.setText(str(int(team_2[myapp.ui.t2_pl1.text()].gold)))
            # myapp.ui.gold_7.setText(str(int(team_2[myapp.ui.t2_pl2.text()].gold)))
            # myapp.ui.gold_8.setText(str(int(team_2[myapp.ui.t2_pl3.text()].gold)))
            # myapp.ui.gold_9.setText(str(int(team_2[myapp.ui.t2_pl4.text()].gold)))
            # myapp.ui.gold_10.setText(str(int(team_2[myapp.ui.t2_pl5.text()].gold)))
            #
            # myapp.ui.net_worth.setText(str(int(team1_net-team2_net)))

        if ev == 'fight':
            t1f = {}
            t2f = {}

            for player in list(team_1.keys()):
                if team_1[player].teamwork >= random.randint(0, 110):
                    a = {player: team_1[player]}
                    t1f.update(a)

            for player in list(team_2.keys()):
                if team_2[player].teamwork >= random.randint(0, 110):
                    a = {player: team_2[player]}
                    t2f.update(a)

            print('+++++++++++++++++++++++')
            print('++++++++FIGHT++++++++++')
            print('+++++++++++++++++++++++')
            #print('Team1', t1f)
            #print('Team2', t2f)

            if len(t1f) == 0 or len(t2f) == 0:
                print('There are no players!')
                if len(t1f) == 0:
                    team1_hp -= random.randint(200,1000)
                if len(t2f) == 0:
                    team2_hp -= random.randint(200,1000)

            else:

                #выяснение эффективности команды#

                t1_sup_ef = 0
                t2_sup_ef = 0

                for player in t1f.keys():
                    if (t1f[player].position == 'Sup') or (t1f[player].position == 'Semi-Sup'):
                        #print(player, 'is sup!')
                        t1_sup_ef += t1f[player].fight
                    else:
                        pass
                for player in t2f.keys():
                    if (t2f[player].position == 'Sup') or (t2f[player].position == 'Semi-Sup'):
                        #print(player, 'is sup!')
                        t2_sup_ef += t2f[player].fight
                    else:
                        pass

                #print('t1sup:', t1_sup_ef)
                #print('t2sup:', t2_sup_ef)


                while (len(t1f) != 0) and (len(t2f) != 0):

                    pick_1 = random.randint(1, len(t1f))
                    pick_2 = random.randint(1, len(t2f))
                    #print('t1fkeys', t1f.keys())
                    #print('t2fkeys', t2f.keys())
                    t1_list = list(t1f.keys())
                    t2_list = list(t2f.keys())
                    #print('t1list:', t1_list)
                    #print('t2list:', t2_list)
                    t1_player = t1f[t1_list[(pick_1-1)]]
                    #print(t1_player)
                    t2_player = t2f[t2_list[(pick_2-1)]]
                    #print(t2_player)

                    p1_killing = t1_player.fight * 1 + t1_sup_ef * 0.25 + random.randint(100, 1000) * 2 + t1_player.gold * 0.02
                    p2_killing = t2_player.fight * 1 + t2_sup_ef * 0.25 + random.randint(100, 1000) * 2 + t2_player.gold * 0.02

                    #print(t1_player.name,':', p1_killing)
                    #print(t2_player.name, ':', p2_killing)

                    if p1_killing > p2_killing:
                        t2f.pop(t2_player.name)
                        t2_player.deaths += 1
                        print("T1 kills T2", t1_player.name, 'killed', t2_player.name, "Assists:", str(t1_list))
                        t1_player.gold += random.randint(100, 900)
                        t1_player.kills += 1
                        t1_player.assists -= 1
                        for player in t1f.keys():
                            t1f[player].assists += 1
                        t1_kills += 1

                    else:
                        t1f.pop(t1_player.name)
                        t1_player.deaths += 1
                        print("T2 kills T1", t2_player.name, 'killed', t1_player.name, "Assists:", str(t2_list))
                        t2_player.gold += random.randint(100, 900)
                        t2_player.kills += 1
                        t2_player.assists -= 1
                        for player in t2f.keys():
                            t2f[player].assists += 1
                        t2_kills += 1

                if len(t1f) == 0:
                    team1_hp -= random.randint(1500, 3000) * len(t2f) * 0.9
                if len(t2f) == 0:
                    team2_hp -= random.randint(1500, 3000) * len(t1f) * 0.9

                print('++++++HEALTH+++++')
                print(int((team1_hp / 20000)*100))
                print(int((team2_hp / 20000)*100))

        # team1_net = int(myapp.ui.gold_1.text()) + int(myapp.ui.gold_2.text()) + int(myapp.ui.gold_3.text()) + int(myapp.ui.gold_4.text()) + int(myapp.ui.gold_5.text())
        # team2_net = int(myapp.ui.gold_6.text()) + int(myapp.ui.gold_7.text()) + int(myapp.ui.gold_8.text()) + int(myapp.ui.gold_9.text()) + int(myapp.ui.gold_10.text())
        #
        # net_worth = team1_net - team2_net
        #
        # myapp.ui.net_worth.setText(str(int(net_worth)))

        t1_hp_pr = int((team1_hp / 20000)*100)
        t2_hp_pr = int((team2_hp / 20000)*100)

        # print('++++++HEALTH+++++')
        # print(t1_hp_pr)
        # print(t2_hp_pr)

        #myapp.ui.t1_hp.setProperty("value", 1)
        #myapp.ui.t2_hp.setProperty("value", 1)

        myapp.ui.team1_hp.setText(str(t1_hp_pr)+'%')
        myapp.ui.team2_hp.setText(str(t2_hp_pr) + '%')


        myapp.ui.t1_kills.setText(str(t1_kills))
        myapp.ui.t2_kills.setText(str(t2_kills))


    max_kills = 0
    max_deaths = 0
    max_assists = 0

    try:
        # KDA Show
        team1_list = []
        for player in team_1:
            if team_1[player].deaths == 0:
                team_1[player].deaths = 1
            team_1[player].kda = round((team_1[player].kills + team_1[player].assists) / team_1[player].deaths, 2)
            team1_list.append(team_1[player])
            if team_1[player].deaths > max_deaths:
                max_deaths = team_1[player].deaths
            if team_1[player].kills > max_kills:
                max_kills = team_1[player].kills
            if team_1[player].assists > max_assists:
                max_assists = team_1[player].assists

        team2_list = []
        for player in team_2:
            if team_2[player].deaths == 0:
                team_2[player].deaths = 1
            team_2[player].kda = round((team_2[player].kills + team_2[player].assists) / team_2[player].deaths, 2)
            team2_list.append(team_2[player])
            if team_2[player].deaths > max_deaths:
                max_deaths = team_2[player].deaths
            if team_2[player].kills > max_kills:
                max_kills = team_2[player].kills
            if team_2[player].assists > max_assists:
                max_assists = team_2[player].assists

        team1_list.sort(key=lambda player: player.kda, reverse=True)
        i = 1
        for player in team1_list:
            kda_stroke = ""
            kda_stroke += str(i) + ". " + '%-15s' % player.name + "  "
            if player.kda >= 0:
                kda_stroke += Fore.GREEN + '%-5s' % str(player.kda) + Style.RESET_ALL + "  " + "("
            else:
                kda_stroke += Fore.RED + '%-5s' % str(player.kda) + Style.RESET_ALL + "  " + "("

            if player.kills == max_kills:
                kda_stroke += Fore.LIGHTYELLOW_EX + str(player.kills) + Style.RESET_ALL + "/"
            else:
                kda_stroke += str(player.kills) + "/"

            if player.assists == max_assists:
                kda_stroke += Fore.GREEN + str(player.assists) + Style.RESET_ALL + "/"
            else:
                kda_stroke += str(player.assists) + "/"

            if player.deaths == max_deaths:
                kda_stroke += Fore.RED + str(player.deaths) + Style.RESET_ALL + ")"
            else:
                kda_stroke += str(player.deaths) + ")"
            i += 1
            print(kda_stroke)

        print('-----team2----')
        team2_list.sort(key=lambda player: player.kda, reverse=True)
        i = 1
        for player in team2_list:
            kda_stroke = ""
            kda_stroke += str(i) + ". " + '%-15s' % player.name + "  "
            if player.kda >= 0:
                kda_stroke += Fore.GREEN + '%-5s' % str(player.kda) + Style.RESET_ALL + "  " + "("
            else:
                kda_stroke += Fore.RED + '%-5s' % str(player.kda) + Style.RESET_ALL + "  " + "("

            if player.kills == max_kills:
                kda_stroke += Fore.LIGHTYELLOW_EX + str(player.kills) + Style.RESET_ALL + "/"
            else:
                kda_stroke += str(player.kills) + "/"

            if player.assists == max_assists:
                kda_stroke += Fore.GREEN + str(player.assists) + Style.RESET_ALL + "/"
            else:
                kda_stroke += str(player.assists) + "/"

            if player.deaths == max_deaths:
                kda_stroke += Fore.RED + str(player.deaths) + Style.RESET_ALL + ")"
            else:
                kda_stroke += str(player.deaths) + ")"
            i += 1
            print(kda_stroke)

    except Exception as e:
        print(e.args[0])



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
