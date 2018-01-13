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


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())