# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coraUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1263, 920)
        MainWindow.setStyleSheet("background-color: rgb(16, 19, 34);\n"
                                 "background-color: rgb(2, 1, 17);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 810, 131, 71))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("            border: none;\n"
                                      "background-color: rgb(103, 147, 200);\n"
                                      "            color: white;\n"
                                      "            padding: 15px 32px;\n"
                                      "            text-align: center;\n"
                                      "            text-decoration: none;\n"
                                      "            display: inline-block;\n"
                                      "            font-size: 16px;\n"
                                      "            margin: 4px 2px;\n"
                                      "            cursor: pointer;\n"
                                      "            border-radius: 10px;\n"
                                      "font: 150 15pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 810, 121, 71))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setStyleSheet("            border: none;\n"
                                        "background-color: rgb(103, 147, 200);\n"
                                        "            color: white;\n"
                                        "            padding: 15px 32px;\n"
                                        "            text-align: center;\n"
                                        "            text-decoration: none;\n"
                                        "            display: inline-block;\n"
                                        "            font-size: 16px;\n"
                                        "            margin: 4px 2px;\n"
                                        "            cursor: pointer;\n"
                                        "            border-radius: 10px;\n"
                                        "font: 150 15pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(910, 30, 256, 51))
        self.textBrowser.setStyleSheet("background:transparent;\n"
                                       "border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(910, 80, 256, 51))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
                                         "border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 820, 741, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("wave.gif"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 391, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Jarvis_Loading_Screen.gif"))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(520, 570, 261, 261))
        self.label.setMinimumSize(QtCore.QSize(261, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("listening_ball.gif"))
        self.label.setObjectName("label")
        self.label_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_2.raise_()
        self.pushButton_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "RUN"))
        self.pushButton_2.setText(_translate("MainWindow", "EXIT"))
