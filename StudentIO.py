import pickle

class Estudiante():
    nombre = '',
    correo = '',
    contrasenia = ''
    def __init__(self, nombre, correo, contrasenia):
        self.nombre = nombre
        self.correo = correo
        self.contrasenia = contrasenia

        # [PV] Los metodos deben estar al mismo nivel de __init__
        def setNombre(self, nombre):
            self.nombre = nombre
        def getNombre(self):
            return self.nombre
        def setCorreo(self, correo):
            self.correo = correo
        def getCorreo(self):
            return self.correo
        def setContrasenia(self, contrasenia):
            self.contrasenia = contrasenia
        def getContrasenia(self):
            return self.contrasenia

objEstudiantes1 = Estudiante('Ana', 'ana.17@gmail.com', '1234')
objEstudiantes2 = Estudiante('Obeth', 'obethd_88@gmail.com', 'qwerty')
objEstudiantes3 = Estudiante('Isamar', 'isa-mg2@gmail.com', 'password')#
objEstudiantes4 = Estudiante('Emmanuel', 'emmanu765@gmail.com', 'loquesea')
objEstudiantes5 = Estudiante('Esmeralda', 'esmerg@gmail.com', 'mascota')
estudiantes = [objEstudiantes1, objEstudiantes2, objEstudiantes3, objEstudiantes4, objEstudiantes5 ]


# [PV] Agrega una lista al archivo, es prefenten objeto a objeto
def agregarEstudiante():
#---------Agregar--------------
    archivo = open('students.db', 'wb')
    pickle.dump(estudiantes, archivo, 5)
    bin_estudiantes = pickle.dumps(estudiantes)
    #print(bin_estudiantes)
    archivo.close()

# [PV] La lectura obtiene una lista, es prefenten objeto a objeto
def leerEstudiante():
#-------Leer-----------------
    file = open('students.db', 'rb')
    file.seek(0)
    unpickler = pickle.Unpickler(file)
    leerEstudiantes = unpickler.load()
    print(leerEstudiantes)   # [PV] Impresion de lista
    file.close()
    for c in leerEstudiantes:  # [PV] Impresion de elementos de la lista
        print('\nNombre:', c.nombre, '\nCorreo: ', c.correo, '\nPassword: ', c.contrasenia)

def modificar():
#---------Modificar----------------
    archivo = open('students.db', 'wb+')
    archivo.seek(0)
    pickle.dump(estudiantes, archivo, 5)
    bin_estudiantes = pickle.dumps(estudiantes)
    archivo.close()


if __name__ == '__main__':
    agregarEstudiante()
    modificar()
    leerEstudiante()