# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main(test).ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(868, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Time = QtWidgets.QLCDNumber(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(450, 0, 221, 81))
        self.Time.setSmallDecimalPoint(False)
        self.Time.setDigitCount(5)
        self.Time.setMode(QtWidgets.QLCDNumber.Dec)
        self.Time.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Time.setProperty("value", 0.0)
        self.Time.setObjectName("Time")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 100, 274, 450))
        self.groupBox.setStatusTip("")
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.registr = QtWidgets.QPushButton(self.groupBox)
        self.registr.setCheckable(False)
        self.registr.setAutoExclusive(False)
        self.registr.setDefault(False)
        self.registr.setFlat(False)
        self.registr.setObjectName("registr")
        self.gridLayout.addWidget(self.registr, 2, 1, 1, 1)
        self.scan = QtWidgets.QPushButton(self.groupBox)
        self.scan.setObjectName("scan")
        self.gridLayout.addWidget(self.scan, 2, 0, 1, 1)
        self.Team2_listWidget = QtWidgets.QListWidget(self.groupBox)
        self.Team2_listWidget.setObjectName("Team2_listWidget")
        self.gridLayout.addWidget(self.Team2_listWidget, 1, 0, 1, 2)
        self.Team1_listWidget = QtWidgets.QListWidget(self.groupBox)
        self.Team1_listWidget.setObjectName("Team1_listWidget")
        self.gridLayout.addWidget(self.Team1_listWidget, 0, 0, 1, 2)
        self.players_init = QtWidgets.QPushButton(self.groupBox)
        self.players_init.setObjectName("players_init")
        self.gridLayout.addWidget(self.players_init, 3, 0, 1, 2)
        self.team1_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.team1_lineEdit.setGeometry(QtCore.QRect(330, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.team1_lineEdit.setFont(font)
        self.team1_lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.team1_lineEdit.setAutoFillBackground(True)
        self.team1_lineEdit.setText("")
        self.team1_lineEdit.setReadOnly(True)
        self.team1_lineEdit.setObjectName("team1_lineEdit")
        self.team2_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.team2_lineEdit.setGeometry(QtCore.QRect(640, 210, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.team2_lineEdit.setFont(font)
        self.team2_lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.team2_lineEdit.setAutoFillBackground(True)
        self.team2_lineEdit.setReadOnly(True)
        self.team2_lineEdit.setClearButtonEnabled(False)
        self.team2_lineEdit.setObjectName("team2_lineEdit")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 270, 231, 157))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.t1_pl3 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t1_pl3.setFont(font)
        self.t1_pl3.setReadOnly(True)
        self.t1_pl3.setObjectName("t1_pl3")
        self.gridLayout_2.addWidget(self.t1_pl3, 2, 1, 1, 1)
        self.t1_pl4 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t1_pl4.setFont(font)
        self.t1_pl4.setReadOnly(True)
        self.t1_pl4.setObjectName("t1_pl4")
        self.gridLayout_2.addWidget(self.t1_pl4, 3, 1, 1, 1)
        self.t1_pl5 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t1_pl5.setFont(font)
        self.t1_pl5.setReadOnly(True)
        self.t1_pl5.setObjectName("t1_pl5")
        self.gridLayout_2.addWidget(self.t1_pl5, 4, 1, 1, 1)
        self.gold_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_3.setFont(font)
        self.gold_3.setObjectName("gold_3")
        self.gridLayout_2.addWidget(self.gold_3, 2, 0, 1, 1)
        self.t1_pl2 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t1_pl2.setFont(font)
        self.t1_pl2.setReadOnly(True)
        self.t1_pl2.setObjectName("t1_pl2")
        self.gridLayout_2.addWidget(self.t1_pl2, 1, 1, 1, 1)
        self.t1_pl1 = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t1_pl1.setFont(font)
        self.t1_pl1.setAutoFillBackground(False)
        self.t1_pl1.setText("")
        self.t1_pl1.setReadOnly(True)
        self.t1_pl1.setObjectName("t1_pl1")
        self.gridLayout_2.addWidget(self.t1_pl1, 0, 1, 1, 1)
        self.gold_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_2.setFont(font)
        self.gold_2.setObjectName("gold_2")
        self.gridLayout_2.addWidget(self.gold_2, 1, 0, 1, 1)
        self.gold_1 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_1.setFont(font)
        self.gold_1.setObjectName("gold_1")
        self.gridLayout_2.addWidget(self.gold_1, 0, 0, 1, 1)
        self.gold_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_5.setFont(font)
        self.gold_5.setObjectName("gold_5")
        self.gridLayout_2.addWidget(self.gold_5, 4, 0, 1, 1)
        self.gold_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_4.setFont(font)
        self.gold_4.setObjectName("gold_4")
        self.gridLayout_2.addWidget(self.gold_4, 3, 0, 1, 1)
        self.t1_hp = QtWidgets.QProgressBar(self.groupBox_2)
        self.t1_hp.setProperty("value", 23)
        self.t1_hp.setInvertedAppearance(False)
        self.t1_hp.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.t1_hp.setObjectName("t1_hp")
        self.gridLayout_2.addWidget(self.t1_hp, 5, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(590, 270, 231, 157))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.t2_pl1 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t2_pl1.setFont(font)
        self.t2_pl1.setReadOnly(True)
        self.t2_pl1.setObjectName("t2_pl1")
        self.gridLayout_3.addWidget(self.t2_pl1, 0, 1, 1, 1)
        self.t2_pl2 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t2_pl2.setFont(font)
        self.t2_pl2.setReadOnly(True)
        self.t2_pl2.setObjectName("t2_pl2")
        self.gridLayout_3.addWidget(self.t2_pl2, 1, 1, 1, 1)
        self.gold_7 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_7.setFont(font)
        self.gold_7.setObjectName("gold_7")
        self.gridLayout_3.addWidget(self.gold_7, 1, 0, 1, 1)
        self.t2_pl5 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t2_pl5.setFont(font)
        self.t2_pl5.setReadOnly(True)
        self.t2_pl5.setObjectName("t2_pl5")
        self.gridLayout_3.addWidget(self.t2_pl5, 4, 1, 1, 1)
        self.gold_6 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_6.setFont(font)
        self.gold_6.setObjectName("gold_6")
        self.gridLayout_3.addWidget(self.gold_6, 0, 0, 1, 1)
        self.t2_pl4 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t2_pl4.setFont(font)
        self.t2_pl4.setReadOnly(True)
        self.t2_pl4.setObjectName("t2_pl4")
        self.gridLayout_3.addWidget(self.t2_pl4, 3, 1, 1, 1)
        self.t2_pl3 = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.t2_pl3.setFont(font)
        self.t2_pl3.setReadOnly(True)
        self.t2_pl3.setObjectName("t2_pl3")
        self.gridLayout_3.addWidget(self.t2_pl3, 2, 1, 1, 1)
        self.gold_8 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_8.setFont(font)
        self.gold_8.setObjectName("gold_8")
        self.gridLayout_3.addWidget(self.gold_8, 2, 0, 1, 1)
        self.gold_10 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_10.setFont(font)
        self.gold_10.setObjectName("gold_10")
        self.gridLayout_3.addWidget(self.gold_10, 4, 0, 1, 1)
        self.gold_9 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Kartika")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gold_9.setFont(font)
        self.gold_9.setObjectName("gold_9")
        self.gridLayout_3.addWidget(self.gold_9, 3, 0, 1, 1)
        self.t2_hp = QtWidgets.QProgressBar(self.groupBox_3)
        self.t2_hp.setProperty("value", 24)
        self.t2_hp.setObjectName("t2_hp")
        self.gridLayout_3.addWidget(self.t2_hp, 5, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 200, 71, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.net_worth = QtWidgets.QLabel(self.centralwidget)
        self.net_worth.setGeometry(QtCore.QRect(510, 220, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.net_worth.setFont(font)
        self.net_worth.setObjectName("net_worth")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(680, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 470, 71, 21))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.team1_hp = QtWidgets.QLabel(self.centralwidget)
        self.team1_hp.setGeometry(QtCore.QRect(350, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.team1_hp.setFont(font)
        self.team1_hp.setObjectName("team1_hp")
        self.team2_hp = QtWidgets.QLabel(self.centralwidget)
        self.team2_hp.setGeometry(QtCore.QRect(660, 440, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.team2_hp.setFont(font)
        self.team2_hp.setObjectName("team2_hp")
        self.t1_kills = QtWidgets.QLabel(self.centralwidget)
        self.t1_kills.setGeometry(QtCore.QRect(360, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t1_kills.setFont(font)
        self.t1_kills.setObjectName("t1_kills")
        self.t2_kills = QtWidgets.QLabel(self.centralwidget)
        self.t2_kills.setGeometry(QtCore.QRect(670, 240, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.t2_kills.setFont(font)
        self.t2_kills.setObjectName("t2_kills")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 600, 871, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.version = QtWidgets.QLabel(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(790, 610, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.version.setFont(font)
        self.version.setObjectName("version")
        self.t1_logo_label = QtWidgets.QLabel(self.centralwidget)
        self.t1_logo_label.setGeometry(QtCore.QRect(330, 100, 151, 101))
        self.t1_logo_label.setObjectName("t1_logo_label")
        self.t2_logo_label = QtWidgets.QLabel(self.centralwidget)
        self.t2_logo_label.setGeometry(QtCore.QRect(640, 90, 151, 101))
        self.t2_logo_label.setObjectName("t2_logo_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuBase_Health = QtWidgets.QMenu(self.menuSettings)
        self.menuBase_Health.setObjectName("menuBase_Health")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action30_000 = QtWidgets.QAction(MainWindow)
        self.action30_000.setObjectName("action30_000")
        self.action20_000 = QtWidgets.QAction(MainWindow)
        self.action20_000.setObjectName("action20_000")
        self.action10_000 = QtWidgets.QAction(MainWindow)
        self.action10_000.setObjectName("action10_000")
        self.menuBase_Health.addAction(self.action30_000)
        self.menuBase_Health.addAction(self.action20_000)
        self.menuBase_Health.addAction(self.action10_000)
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.menuBase_Health.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Выбор команд:"))
        self.registr.setText(_translate("MainWindow", "Зарегистрировать"))
        self.scan.setText(_translate("MainWindow", "Сканировать"))
        self.players_init.setText(_translate("MainWindow", "Инициализировать игроков"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Игроки:"))
        self.gold_3.setText(_translate("MainWindow", "TextLabel"))
        self.gold_2.setText(_translate("MainWindow", "TextLabel"))
        self.gold_1.setText(_translate("MainWindow", "TextLabel"))
        self.gold_5.setText(_translate("MainWindow", "TextLabel"))
        self.gold_4.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Игроки:"))
        self.gold_7.setText(_translate("MainWindow", "TextLabel"))
        self.gold_6.setText(_translate("MainWindow", "TextLabel"))
        self.gold_8.setText(_translate("MainWindow", "TextLabel"))
        self.gold_10.setText(_translate("MainWindow", "TextLabel"))
        self.gold_9.setText(_translate("MainWindow", "TextLabel"))
        self.label.setText(_translate("MainWindow", "Net Worth"))
        self.net_worth.setText(_translate("MainWindow", "0000"))
        self.label_2.setText(_translate("MainWindow", "min"))
        self.team1_hp.setText(_translate("MainWindow", "team1_hp"))
        self.team2_hp.setText(_translate("MainWindow", "team2_hp"))
        self.t1_kills.setText(_translate("MainWindow", "TextLabel"))
        self.t2_kills.setText(_translate("MainWindow", "TextLabel"))
        self.version.setText(_translate("MainWindow", "Version"))
        self.t1_logo_label.setText(_translate("MainWindow", "TextLabel"))
        self.t2_logo_label.setText(_translate("MainWindow", "TextLabel"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuBase_Health.setTitle(_translate("MainWindow", "Base Health"))
        self.action30_000.setText(_translate("MainWindow", "30 000"))
        self.action20_000.setText(_translate("MainWindow", "20 000"))
        self.action10_000.setText(_translate("MainWindow", "10 000"))

