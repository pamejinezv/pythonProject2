from mongoengine import *


connect('IECA', host='localhost', port=27017)

class estudiantes(Document):
    nombre = '',
    correo = '',
    contrasenia = '',

    nombre = StringField(required=True, max_length=50)
    correo = StringField(required=True, max_length=100)
    contrasenia = StringField(required=True, max_length=20)
    materias = ListField()

class administradora:

    def guardar():
        nombre = input('Escribe el nombre')
        correo = input('Escribe el correo')
        passw = input('Escribe la contrasenia')
        cantidad = int(input('Escribe la cantidad de materias tendra tu estudiante\n'))
        nombresMaterias = []
        for i in range(cantidad):
            nomMateria = input('Escribe el nombre de la materia')
            nombresMaterias.append(nomMateria)

        post = estudiantes(
            nombre=nombre,
            correo=correo,
            contrasenia=passw,
            materias=nombresMaterias
        )
        post.save()

        print('Datos almacenados con exito')

    def eliminar():
        nomAlumno = input('Escribe el nombre del alumno a eliminar')
        post = estudiantes.objects(nombre=nomAlumno)
        post.delete()
        print('Datos eliminados con exito')

    def modificar():
        nomAlumno = input('Escribe el nombre del alumno a modificar')
        correo = input('Escribe el correo')
        passw = input('Escribe la contrasenia')
        student = estudiantes.objects(nombre=nomAlumno)
        fields={
            'correo':correo,
            'contrasenia':passw
        }
        student.update(**fields)
        print('Datos actualizados con exito')

    def mostrarTodo():
        post = estudiantes.objects.all_fields()
        for c in post:
            print('\nNombre:', c.nombre, '\nCorreo: ', c.correo, '\nPassword: ', c.contrasenia)

    def menu():
        while True:
            print('-----MENU-----')
            print('**Opcion 1: AGREGAR**')
            print('**Opcion 2: MOSTRAR TODO**')
            print('**Opcion 3: ELIMINAR**')
            print('**Opcion 4: MODIFICAR**')
            print('**Opcion 5: SALIR**')

            opcion = int(input('Escriba el numero que corresponda a la operacion que va a realizar: '))
            if opcion == 1:
                administradora.guardar()
            elif opcion == 2:
                administradora.mostrarTodo()
            elif opcion == 3:
                administradora.eliminar()
            elif opcion == 4:
                administradora.modificar()
            elif opcion == 5:
                break
if __name__ == '__main__':

   administradora.menu()