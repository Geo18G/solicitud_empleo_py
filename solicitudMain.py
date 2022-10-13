import sys
from PyQt5.QtWidgets import *
from interfaz import interfaz_UI
from verificar import Ui_verificar

class verificar(QMainWindow):
    def __init__(self):
        super(verificar, self).__init__()
        self.ui2 = Ui_verificar()
        self.ui2.setupUi(self)

class solicitud(QMainWindow):
    def __init__(self):
        super(solicitud, self).__init__()
        self.ui = interfaz_UI()
        self.ui.setupUi(self)
        self.verificar = verificar()
        self.inicializar()

    def inicializar(self):
        self.ui.btn_enviar.setEnabled(False)
        self.ui.btn_cerrar.clicked.connect(lambda: self.close())
        self.ui.nombre.textChanged.connect(self.habilitarEnviar)
        self.ui.edad.textChanged.connect(self.habilitarEnviar)
        self.ui.btn_enviar.clicked.connect(self.verificarEvent)
        self.verificar.ui2.pushButton.clicked.connect(lambda: self.close())
        self.verificar.ui2.pushButton.clicked.connect(lambda: self.verificar.close())
        self.verificar.ui2.pushButton_2.clicked.connect(lambda: self.verificar.close())
        

    def habilitarEnviar(self):
        if self.ui.nombre.text() == "" or self.ui.edad.text() == "":
            self.ui.btn_enviar.setEnabled(False)
        else:
            self.ui.btn_enviar.setEnabled(True)

    def verificarEvent(self):
        self.verificar.show()
        self.verificar.ui2.nombre.setText(f"Nombre: {self.ui.nombre.text()}")
        self.verificar.ui2.edad.setText(f"Edad: {self.ui.edad.text()}")
        if self.ui.lgbt.isChecked():
            self.verificar.ui2.genero.setText("Genero: LGBT+")
        elif self.ui.femenino.isChecked():
            self.verificar.ui2.genero.setText("Genero: Femenino")
        else:
            self.verificar.ui2.genero.setText("Genero: Masculino") 
        listaActividades = [self.ui.electricidad, self.ui.programacion, self.ui.electronica, self.ui.administracion, self.ui.otro]
        for act in listaActividades:
            if act.isChecked():
                text = self.verificar.ui2.actividades.text()
                self.verificar.ui2.actividades.setText(f"{text + act.text()}, ")
        self.verificar.ui2.grado.setText("Grado de estudios: " + self.ui.grado_estudios.currentText())
        self.verificar.ui2.experiencia.setText("Años de experiencia: " + self.ui.anios_exp.text())

if __name__ == "__main__":
    app = QApplication([])
    myApp = solicitud()
    myApp.show()
    sys.exit(app.exec_())
