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
        self.Time.setGeometry(QtCore.QRect(340, 0, 221, 81))
        self.Time.setObjectName("Time")
        self.Team1 = QtWidgets.QListView(self.centralwidget)
        self.Team1.setGeometry(QtCore.QRect(20, 120, 256, 192))
        font = QtGui.QFont()
        font.setFamily("Raavi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Team1.setFont(font)
        self.Team1.setAutoFillBackground(False)
        self.Team1.setSelectionRectVisible(True)
        self.Team1.setObjectName("Team1")
        self.Team2 = QtWidgets.QListView(self.centralwidget)
        self.Team2.setGeometry(QtCore.QRect(20, 320, 256, 192))
        font = QtGui.QFont()
        font.setFamily("Raavi")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Team2.setFont(font)
        self.Team2.setAutoFillBackground(False)
        self.Team2.setSelectionRectVisible(True)
        self.Team2.setObjectName("Team2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 868, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBase_Health = QtWidgets.QAction(MainWindow)
        self.actionBase_Health.setObjectName("actionBase_Health")
        self.menuSettings.addSeparator()
        self.menuSettings.addAction(self.actionBase_Health)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionBase_Health.setText(_translate("MainWindow", "Base Health"))

