# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'verificar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_verificar(object):
    def setupUi(self, verificar):
        verificar.setObjectName("verificar")
        verificar.resize(615, 445)
        verificar.setMinimumSize(QtCore.QSize(615, 445))
        verificar.setMaximumSize(QtCore.QSize(615, 445))
        self.centralwidget = QtWidgets.QWidget(verificar)
        self.centralwidget.setObjectName("centralwidget")
        self.nombre = QtWidgets.QLabel(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(30, 30, 281, 41))
        self.nombre.setObjectName("nombre")
        self.experiencia = QtWidgets.QLabel(self.centralwidget)
        self.experiencia.setGeometry(QtCore.QRect(30, 330, 281, 41))
        self.experiencia.setObjectName("experiencia")
        self.genero = QtWidgets.QLabel(self.centralwidget)
        self.genero.setGeometry(QtCore.QRect(30, 150, 281, 41))
        self.genero.setObjectName("genero")
        self.edad = QtWidgets.QLabel(self.centralwidget)
        self.edad.setGeometry(QtCore.QRect(30, 90, 281, 41))
        self.edad.setObjectName("edad")
        self.grado = QtWidgets.QLabel(self.centralwidget)
        self.grado.setGeometry(QtCore.QRect(30, 210, 281, 41))
        self.grado.setObjectName("grado")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 380, 93, 28))
        self.pushButton_2.setObjectName("cancelar")
        self.actividades = QtWidgets.QLabel(self.centralwidget)
        self.actividades.setGeometry(QtCore.QRect(30, 270, 551, 41))
        self.actividades.setObjectName("actividades")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 380, 93, 28))
        self.pushButton.setObjectName("registrar")
        verificar.setCentralWidget(self.centralwidget)

        self.retranslateUi(verificar)
        QtCore.QMetaObject.connectSlotsByName(verificar)

    def retranslateUi(self, verificar):
        _translate = QtCore.QCoreApplication.translate
        verificar.setWindowTitle(_translate("verificar", "Verificar sus Datos"))
        self.nombre.setText(_translate("verificar", "Nombre"))
        self.experiencia.setText(_translate("verificar", "Expericencia"))
        self.genero.setText(_translate("verificar", "Genero"))
        self.edad.setText(_translate("verificar", "edad"))
        self.grado.setText(_translate("verificar", "Grado"))
        self.pushButton_2.setText(_translate("verificar", "Cancelar"))
        self.actividades.setText(_translate("verificar", "Actividades: "))
        self.pushButton.setText(_translate("verificar", "Registrar"))
