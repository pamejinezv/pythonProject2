# from Tarea5.InterfazT5 import *
# [PV] No es necesario Tarea5
from InterfazT5 import *
from mongoengine import *
import re
import sys

connect('IECA', host='localhost', port=27017)
class Practica(QMainWindow):

    def __init__(self):
        super(Practica, self).__init__()
        self.ui = Ui_Practica()
        self.ui.setupUi(self)

        self.ui.btnEditar.setEnabled(False)
        self.ui.btnGuardar.setEnabled(False)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnMostrar.clicked.connect(self.mostrarUno)
        self.ui.btnEditar.clicked.connect(self.modificar)
        self.ui.txtNombre.textEdited.connect(self.textoEditado)
        self.ui.txtCorreo.textEdited.connect(self.textoEditado)
        self.ui.txtPass.textEdited.connect(self.textoEditado)
        self.ui.txtNombre.clear()
        self.ui.txtCorreo.clear()
        self.ui.txtPass.clear()
        self.ui.lblId.setVisible(False)


    def textoEditado(self):
        if ((len(self.ui.txtNombre.text()) >= 1) and (len(self.ui.txtCorreo.text()) >= 1)  and (len(self.ui.txtPass.text()) >= 1)):
            self.ui.btnGuardar.setEnabled(True)
        else:
            self.ui.btnGuardar.setEnabled(False)

    def guardar(self):

        nombre = self.ui.txtNombre.text()
        correo = self.ui.txtCorreo.text()
        passw = self.ui.txtPass.text()
        post = estudiantes(
            nombre=nombre,
            correo=correo,
            passw=passw
        )
        self.validaCorreo(resp= False)
        self.validaPass(resp=False)
        if (self.validaCorreo(True)) and (self.validaPass(True)):
            post.save()
            self.ui.btnGuardar.setEnabled(False)
            self.ui.txtNombre.setFocus()
            print('Datos almacenados con exito')
            self.ui.txtNombre.clear()
            self.ui.txtCorreo.clear()
            self.ui.txtPass.clear()

    pass

    def validaCorreo(self, resp):
        correo = self.ui.txtCorreo.text()
        patron = '^[(a-zA-Z0-9\_\-\.)]+@[(a-zA-Z\_\-\.)]+\.[(a-zA-Z)]{2,}$'
        valida = re.match(patron, correo)
        if valida:
            return resp == True
        else:
            print('Correo electronico Incorrecto, escribalo nuevamente')


    def validaPass(self, resp):
        passw = self.ui.txtPass.text()
        patron = '^[a-zA-Z0-9]{8,}$'
        valida = re.search(patron, passw)
        if valida:
            return resp == True
        else:
            print('Contraseña poco segura, escriba una nuevamente al menos 8 digitos solo numeros y letras')



    def mostrarUno(self):
        nombreBuscar = self.ui.txtNombre.text()
        post = estudiantes.objects(nombre=nombreBuscar).first()
        if post:
            self.ui.txtCorreo.clear()
            self.ui.txtPass.clear()
            self.ui.lblId.setText(post.nombre)
            self.ui.txtCorreo.setText(post.correo)
            self.ui.txtPass.setText(post.passw)
            self.ui.btnEditar.setEnabled(True)
            self.ui.btnGuardar.setEnabled(False)
        else:
            self.ui.txtCorreo.clear()
            self.ui.txtPass.clear()
            print('No hay informacion con el nombre especificado, escriba otro')
            self.ui.txtNombre.setFocus()
            self.ui.btnEditar.setEnabled(False)
            self.ui.txtNombre.clear()

    def modificar(self):
        nomAlumno = self.ui.txtNombre.text()
        correo = self.ui.txtCorreo.text()
        passw = self.ui.txtPass.text()
        student = estudiantes.objects(nombre=self.ui.lblId.text())
        fields = {
            'nombre': nomAlumno,
            'correo': correo,
            'passw': passw
        }
        self.validaCorreo(resp=False)
        self.validaPass(resp=False)
        if ((self.validaCorreo(True))and(self.validaPass(True))):
            student.update(**fields)
            print('Datos actualizados con exito')
            self.ui.btnGuardar.setEnabled(False)
            self.ui.btnEditar.setEnabled(False)
            self.ui.txtNombre.clear()
            self.ui.txtCorreo.clear()
            self.ui.txtPass.clear()


class estudiantes(Document):
    nombre = '',
    correo = '',
    passw = '',

    nombre = StringField(required=True, max_length=50)
    correo = StringField(required=True, max_length=100)
    passw = StringField(required=True, max_length=20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Practica()
    window.show()
    sys.exit(app.exec_())