# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 480)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(174, 247, 255);e")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -10, 461, 541))
        self.stackedWidget.setStyleSheet("background-color: rgb(174, 247, 255);e")
        self.stackedWidget.setObjectName("stackedWidget")
        self.LoginPage = QtWidgets.QWidget()
        self.LoginPage.setObjectName("LoginPage")
        self.Password = QtWidgets.QLineEdit(self.LoginPage)
        self.Password.setGeometry(QtCore.QRect(150, 170, 231, 31))
        self.Password.setText("")
        self.Password.setObjectName("Password")
        self.passwdlabel = QtWidgets.QLabel(self.LoginPage)
        self.passwdlabel.setGeometry(QtCore.QRect(40, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.passwdlabel.setFont(font)
        self.passwdlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.passwdlabel.setObjectName("passwdlabel")
        self.warningp2 = QtWidgets.QLabel(self.LoginPage)
        self.warningp2.setGeometry(QtCore.QRect(90, 240, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.warningp2.setFont(font)
        self.warningp2.setObjectName("warningp2")
        self.Username = QtWidgets.QLineEdit(self.LoginPage)
        self.Username.setGeometry(QtCore.QRect(150, 110, 231, 31))
        self.Username.setText("")
        self.Username.setObjectName("Username")
        self.Remember = QtWidgets.QCheckBox(self.LoginPage)
        self.Remember.setGeometry(QtCore.QRect(290, 230, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Remember.setFont(font)
        self.Remember.setObjectName("Remember")
        self.LoginButton = QtWidgets.QPushButton(self.LoginPage)
        self.LoginButton.setGeometry(QtCore.QRect(70, 290, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LoginButton.setFont(font)
        self.LoginButton.setStyleSheet("color: white;\n"
"background-color:#32a852")
        self.LoginButton.setAutoRepeat(False)
        self.LoginButton.setAutoRepeatDelay(300)
        self.LoginButton.setObjectName("LoginButton")
        self.usrlabel = QtWidgets.QLabel(self.LoginPage)
        self.usrlabel.setGeometry(QtCore.QRect(40, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usrlabel.setFont(font)
        self.usrlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usrlabel.setObjectName("usrlabel")
        self.LoginLabel = QtWidgets.QLabel(self.LoginPage)
        self.LoginLabel.setGeometry(QtCore.QRect(0, 0, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setStyleSheet("color:rgb(140, 255, 154);")
        self.LoginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginLabel.setObjectName("LoginLabel")
        self.warningp1 = QtWidgets.QLabel(self.LoginPage)
        self.warningp1.setGeometry(QtCore.QRect(90, 220, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.warningp1.setFont(font)
        self.warningp1.setObjectName("warningp1")
        self.stackedWidget.addWidget(self.LoginPage)
        self.LoadingPage = QtWidgets.QWidget()
        self.LoadingPage.setObjectName("LoadingPage")
        self.label_8 = QtWidgets.QLabel(self.LoadingPage)
        self.label_8.setGeometry(QtCore.QRect(40, 150, 401, 151))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.LoadingPage)
        self.SettingsPage = QtWidgets.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.AutoMove = QtWidgets.QCheckBox(self.SettingsPage)
        self.AutoMove.setGeometry(QtCore.QRect(90, 280, 81, 21))
        self.AutoMove.setObjectName("AutoMove")
        self.RThinkingTime = QtWidgets.QCheckBox(self.SettingsPage)
        self.RThinkingTime.setGeometry(QtCore.QRect(90, 360, 261, 21))
        self.RThinkingTime.setObjectName("RThinkingTime")
        self.label_2 = QtWidgets.QLabel(self.SettingsPage)
        self.label_2.setGeometry(QtCore.QRect(100, 90, 91, 21))
        self.label_2.setObjectName("label_2")
        self.StockFishlevel = QtWidgets.QScrollBar(self.SettingsPage)
        self.StockFishlevel.setGeometry(QtCore.QRect(200, 90, 121, 16))
        self.StockFishlevel.setStyleSheet("background-color: #32a852;")
        self.StockFishlevel.setMinimum(1)
        self.StockFishlevel.setMaximum(25)
        self.StockFishlevel.setProperty("value", 4)
        self.StockFishlevel.setOrientation(QtCore.Qt.Horizontal)
        self.StockFishlevel.setObjectName("StockFishlevel")
        self.label_3 = QtWidgets.QLabel(self.SettingsPage)
        self.label_3.setGeometry(QtCore.QRect(90, 320, 101, 21))
        self.label_3.setObjectName("label_3")
        self.thinkingTime = QtWidgets.QScrollBar(self.SettingsPage)
        self.thinkingTime.setGeometry(QtCore.QRect(190, 320, 121, 16))
        self.thinkingTime.setStyleSheet("background-color: #32a852;")
        self.thinkingTime.setMinimum(0)
        self.thinkingTime.setMaximum(400)
        self.thinkingTime.setOrientation(QtCore.Qt.Horizontal)
        self.thinkingTime.setObjectName("thinkingTime")
        self.MovesAhead = QtWidgets.QScrollBar(self.SettingsPage)
        self.MovesAhead.setGeometry(QtCore.QRect(200, 130, 121, 16))
        self.MovesAhead.setStyleSheet("background-color: #32a852;")
        self.MovesAhead.setMinimum(1)
        self.MovesAhead.setMaximum(30)
        self.MovesAhead.setOrientation(QtCore.Qt.Horizontal)
        self.MovesAhead.setObjectName("MovesAhead")
        self.label_4 = QtWidgets.QLabel(self.SettingsPage)
        self.label_4.setGeometry(QtCore.QRect(100, 130, 71, 16))
        self.label_4.setObjectName("label_4")
        self.Rstockfishlevelcheck = QtWidgets.QCheckBox(self.SettingsPage)
        self.Rstockfishlevelcheck.setGeometry(QtCore.QRect(90, 180, 181, 21))
        self.Rstockfishlevelcheck.setObjectName("Rstockfishlevelcheck")
        self.RSLFROM = QtWidgets.QSpinBox(self.SettingsPage)
        self.RSLFROM.setGeometry(QtCore.QRect(280, 180, 42, 22))
        self.RSLFROM.setMinimum(1)
        self.RSLFROM.setMaximum(24)
        self.RSLFROM.setObjectName("RSLFROM")
        self.RSLTO = QtWidgets.QSpinBox(self.SettingsPage)
        self.RSLTO.setGeometry(QtCore.QRect(350, 180, 42, 22))
        self.RSLTO.setMinimum(2)
        self.RSLTO.setMaximum(25)
        self.RSLTO.setObjectName("RSLTO")
        self.label_5 = QtWidgets.QLabel(self.SettingsPage)
        self.label_5.setGeometry(QtCore.QRect(330, 180, 16, 16))
        self.label_5.setObjectName("label_5")
        self.Rmovesaheadcheck = QtWidgets.QCheckBox(self.SettingsPage)
        self.Rmovesaheadcheck.setGeometry(QtCore.QRect(90, 230, 181, 21))
        self.Rmovesaheadcheck.setObjectName("Rmovesaheadcheck")
        self.RMAFROM = QtWidgets.QSpinBox(self.SettingsPage)
        self.RMAFROM.setGeometry(QtCore.QRect(280, 230, 42, 22))
        self.RMAFROM.setMinimum(1)
        self.RMAFROM.setMaximum(29)
        self.RMAFROM.setObjectName("RMAFROM")
        self.RMATO = QtWidgets.QSpinBox(self.SettingsPage)
        self.RMATO.setGeometry(QtCore.QRect(350, 230, 42, 22))
        self.RMATO.setMinimum(2)
        self.RMATO.setMaximum(30)
        self.RMATO.setObjectName("RMATO")
        self.label_6 = QtWidgets.QLabel(self.SettingsPage)
        self.label_6.setGeometry(QtCore.QRect(330, 230, 16, 16))
        self.label_6.setObjectName("label_6")
        self.Title = QtWidgets.QLabel(self.SettingsPage)
        self.Title.setGeometry(QtCore.QRect(130, 20, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: #32a852;")
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Start = QtWidgets.QPushButton(self.SettingsPage)
        self.Start.setGeometry(QtCore.QRect(90, 400, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Start.setFont(font)
        self.Start.setStyleSheet("color: white;\n"
"background-color:#32a852")
        self.Start.setObjectName("Start")
        self.levelLabel = QtWidgets.QLabel(self.SettingsPage)
        self.levelLabel.setGeometry(QtCore.QRect(340, 90, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.levelLabel.setFont(font)
        self.levelLabel.setObjectName("levelLabel")
        self.movesLabel = QtWidgets.QLabel(self.SettingsPage)
        self.movesLabel.setGeometry(QtCore.QRect(340, 130, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.movesLabel.setFont(font)
        self.movesLabel.setObjectName("movesLabel")
        self.thinkingLabel = QtWidgets.QLabel(self.SettingsPage)
        self.thinkingLabel.setGeometry(QtCore.QRect(330, 320, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.thinkingLabel.setFont(font)
        self.thinkingLabel.setObjectName("thinkingLabel")
        self.stackedWidget.addWidget(self.SettingsPage)
        self.BotPage = QtWidgets.QWidget()
        self.BotPage.setObjectName("BotPage")
        self.StopButton = QtWidgets.QPushButton(self.BotPage)
        self.StopButton.setGeometry(QtCore.QRect(80, 360, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.StopButton.setFont(font)
        self.StopButton.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);")
        self.StopButton.setObjectName("StopButton")
        self.label = QtWidgets.QLabel(self.BotPage)
        self.label.setGeometry(QtCore.QRect(110, 260, 231, 16))
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.BotPage)
        self.label_7.setGeometry(QtCore.QRect(130, 280, 201, 20))
        self.label_7.setObjectName("label_7")
        self.BestMove = QtWidgets.QLabel(self.BotPage)
        self.BestMove.setGeometry(QtCore.QRect(30, 30, 371, 161))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.BestMove.setFont(font)
        self.BestMove.setText("")
        self.BestMove.setAlignment(QtCore.Qt.AlignCenter)
        self.BestMove.setObjectName("BestMove")
        self.timeToMove = QtWidgets.QLabel(self.BotPage)
        self.timeToMove.setGeometry(QtCore.QRect(170, 320, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timeToMove.setFont(font)
        self.timeToMove.setText("")
        self.timeToMove.setAlignment(QtCore.Qt.AlignCenter)
        self.timeToMove.setObjectName("timeToMove")
        self.stackedWidget.addWidget(self.BotPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.MovesAhead.valueChanged['int'].connect(self.movesLabel.setNum)
        self.StockFishlevel.valueChanged['int'].connect(self.levelLabel.setNum)
        self.thinkingTime.valueChanged['int'].connect(self.thinkingLabel.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chess Bot"))
        self.stackedWidget.setAccessibleDescription(_translate("MainWindow", "background-color: rgb(174, 247, 255);e"))
        self.passwdlabel.setText(_translate("MainWindow", "Password"))
        self.warningp2.setText(_translate("MainWindow", "just log in manually on the page"))
        self.Remember.setText(_translate("MainWindow", "Remember"))
        self.LoginButton.setText(_translate("MainWindow", "Login"))
        self.usrlabel.setText(_translate("MainWindow", "Username"))
        self.LoginLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#32a852;\">Login into your chess.com account:</span></p></body></html>"))
        self.warningp1.setText(_translate("MainWindow", "*If you passed wrong data"))
        self.label_8.setText(_translate("MainWindow", "LOADING..."))
        self.AutoMove.setText(_translate("MainWindow", "AutoMove"))
        self.RThinkingTime.setText(_translate("MainWindow", "Random thinking time *between 0 and  set time"))
        self.label_2.setText(_translate("MainWindow", "Stockfish Level"))
        self.label_3.setText(_translate("MainWindow", "Thinking time(sec)"))
        self.label_4.setText(_translate("MainWindow", "Moves ahead"))
        self.Rstockfishlevelcheck.setText(_translate("MainWindow", "Random stockfish level between"))
        self.label_5.setText(_translate("MainWindow", "-"))
        self.Rmovesaheadcheck.setText(_translate("MainWindow", "Random moves ahead between"))
        self.label_6.setText(_translate("MainWindow", "-"))
        self.Title.setText(_translate("MainWindow", "Set your BOT up"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.levelLabel.setText(_translate("MainWindow", "1"))
        self.movesLabel.setText(_translate("MainWindow", "1"))
        self.thinkingLabel.setText(_translate("MainWindow", "1"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.label.setText(_translate("MainWindow", "*If you want change settings during the game"))
        self.label_7.setText(_translate("MainWindow", "just rerun the bot using Stop button"))
