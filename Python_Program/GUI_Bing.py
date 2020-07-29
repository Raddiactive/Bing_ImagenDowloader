# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bing.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Obtener = QtWidgets.QPushButton(self.centralwidget)
        self.Obtener.setGeometry(QtCore.QRect(50, 31, 112, 25))
        self.Obtener.setObjectName("Obtener")
        self.Previsualizar = QtWidgets.QPushButton(self.centralwidget)
        self.Previsualizar.setGeometry(QtCore.QRect(166, 31, 95, 25))
        self.Previsualizar.setObjectName("Previsualizar")
        self.Ruta = QtWidgets.QPushButton(self.centralwidget)
        self.Ruta.setGeometry(QtCore.QRect(265, 31, 80, 25))
        self.Ruta.setObjectName("Ruta")
        self.Imagen = QtWidgets.QLabel(self.centralwidget)
        self.Imagen.setGeometry(QtCore.QRect(56, 106, 681, 401))
        self.Imagen.setText("")
        self.Imagen.setObjectName("Imagen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Obtener.setText(_translate("MainWindow", "Get image"))
        self.Previsualizar.setText(_translate("MainWindow", "Preview"))
        self.Ruta.setText(_translate("MainWindow", "Deviate"))
