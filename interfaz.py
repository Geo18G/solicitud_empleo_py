# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solicitud.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class interfaz_UI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1039, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, -20, 471, 91))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 971, 191))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.nombre = QtWidgets.QLineEdit(self.groupBox)
        self.nombre.setGeometry(QtCore.QRect(190, 40, 601, 31))
        self.nombre.setObjectName("nombre")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 171, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(110, 110, 71, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(370, 110, 71, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.masculino = QtWidgets.QRadioButton(self.groupBox)
        self.masculino.setGeometry(QtCore.QRect(460, 90, 111, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.masculino.setFont(font)
        self.masculino.setChecked(True)
        self.masculino.setObjectName("masculino")
        self.femenino = QtWidgets.QRadioButton(self.groupBox)
        self.femenino.setGeometry(QtCore.QRect(460, 120, 121, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.femenino.setFont(font)
        self.femenino.setObjectName("femenino")
        self.lgbt = QtWidgets.QRadioButton(self.groupBox)
        self.lgbt.setGeometry(QtCore.QRect(460, 150, 101, 17))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lgbt.setFont(font)
        self.lgbt.setObjectName("lgbt")
        self.edad = QtWidgets.QLineEdit(self.groupBox)
        self.edad.setGeometry(QtCore.QRect(170, 110, 51, 31))
        self.edad.setObjectName("edad")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 270, 981, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(490, 50, 191, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.grado_estudios = QtWidgets.QComboBox(self.groupBox_2)
        self.grado_estudios.setGeometry(QtCore.QRect(260, 40, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.grado_estudios.setFont(font)
        self.grado_estudios.setObjectName("grado_estudios")
        self.grado_estudios.addItem("")
        self.grado_estudios.addItem("")
        self.grado_estudios.addItem("")
        self.grado_estudios.addItem("")
        self.grado_estudios.addItem("")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 241, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.anios_exp = QtWidgets.QSpinBox(self.groupBox_2)
        self.anios_exp.setGeometry(QtCore.QRect(710, 50, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.anios_exp.setFont(font)
        self.anios_exp.setPrefix("")
        self.anios_exp.setProperty("value", 1)
        self.anios_exp.setObjectName("anios_exp")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 110, 271, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.electricidad = QtWidgets.QCheckBox(self.groupBox_2)
        self.electricidad.setGeometry(QtCore.QRect(290, 110, 121, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.electricidad.setFont(font)
        self.electricidad.setChecked(True)
        self.electricidad.setObjectName("electricidad")
        self.programacion = QtWidgets.QCheckBox(self.groupBox_2)
        self.programacion.setGeometry(QtCore.QRect(290, 130, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.programacion.setFont(font)
        self.programacion.setObjectName("programacion")
        self.electronica = QtWidgets.QCheckBox(self.groupBox_2)
        self.electronica.setGeometry(QtCore.QRect(290, 150, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.electronica.setFont(font)
        self.electronica.setObjectName("electronica")
        self.administracion = QtWidgets.QCheckBox(self.groupBox_2)
        self.administracion.setGeometry(QtCore.QRect(290, 170, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.administracion.setFont(font)
        self.administracion.setObjectName("administracion")
        self.otro = QtWidgets.QCheckBox(self.groupBox_2)
        self.otro.setGeometry(QtCore.QRect(290, 190, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.otro.setFont(font)
        self.otro.setObjectName("otro")
        self.metas = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.metas.setGeometry(QtCore.QRect(480, 110, 401, 101))
        self.metas.setObjectName("metas")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(480, 90, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(770, 550, 211, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_enviar = QtWidgets.QPushButton(self.frame)
        self.btn_enviar.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.btn_enviar.setObjectName("btn_enviar")
        self.btn_cerrar = QtWidgets.QPushButton(self.frame)
        self.btn_cerrar.setGeometry(QtCore.QRect(130, 20, 75, 23))
        self.btn_cerrar.setObjectName("btn_cerrar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1039, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "SOLICITUD DE TRABAJO"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos generales"))
        self.label_2.setText(_translate("MainWindow", "Nombre completo:"))
        self.label_3.setText(_translate("MainWindow", "Edad:"))
        self.label_4.setText(_translate("MainWindow", "Género:"))
        self.masculino.setText(_translate("MainWindow", "Masculino"))
        self.femenino.setText(_translate("MainWindow", "Femenino"))
        self.lgbt.setText(_translate("MainWindow", "LGBT"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Experiencia"))
        self.label_5.setText(_translate("MainWindow", "Años de experiencia:"))
        self.grado_estudios.setItemText(0, _translate("MainWindow", "Primaria"))
        self.grado_estudios.setItemText(1, _translate("MainWindow", "Secundaria"))
        self.grado_estudios.setItemText(2, _translate("MainWindow", "Preparatoria"))
        self.grado_estudios.setItemText(3, _translate("MainWindow", "Grado"))
        self.grado_estudios.setItemText(4, _translate("MainWindow", "Posgrado"))
        self.label_6.setText(_translate("MainWindow", "Ultimo grado de estudios:"))
        self.label_7.setText(_translate("MainWindow", "Actividades que sabe realizar:"))
        self.electricidad.setText(_translate("MainWindow", "Electricidad"))
        self.programacion.setText(_translate("MainWindow", "Programación"))
        self.electronica.setText(_translate("MainWindow", "Electrónica"))
        self.administracion.setText(_translate("MainWindow", "Administración"))
        self.otro.setText(_translate("MainWindow", "Otro"))
        self.label_8.setText(_translate("MainWindow", "¿Cuales son tus metas a corto plazo?"))
        self.btn_enviar.setText(_translate("MainWindow", "ENVIAR"))
        self.btn_cerrar.setText(_translate("MainWindow", "CERRAR"))
