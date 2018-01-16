import os
from PyQt5 import QtWidgets, QtGui
from forms import test
import sys
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

        self.ui.registr.clicked.connect(self.set_first_team)

        self.ui.players_init.clicked.connect(initialize_players)

    def scanning(self):

        self.ui.Team1_listWidget.clear()
        self.ui.Team2_listWidget.clear()

        appPath = os.path.dirname(os.path.realpath(__file__))
        dir_list = os.listdir(appPath)
        print(dir_list)
        self.ui.Team1_listWidget.addItems(dir_list)
        self.ui.Team2_listWidget.addItems(dir_list)

        msgbox = UI_Dialog()
        msgbox.show_msg_box('Сканированно!', 'SCAN')


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


def initialize_players():
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

    return [team_1, team_2]








if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())