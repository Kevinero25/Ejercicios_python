"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda
"""



class Agenda:
    def __init__(self):
        self.contactos = []

    def menu(self):
        print()
        menu = [
            
            ['1. Añadir Contacto'],
            ['2. Lista de contactos'],
            ['3. Buscar contacto'],
            ['4. Editar contacto'],
            ['5. Cerrar agenda']
        ]

        for opcion in menu:
            print(opcion[0])

        opcion = int(input("Escoje la opcion!: "))

        if opcion == 1:
            self.anadir()
        elif opcion == 2:
            self.lista()
        elif opcion == 3:
            self.buscar()
        elif opcion == 4:
            self.editar()
        elif opcion == 5:
            print("Saliendo de la agenda ...")
            exit()

        self.menu()

    def anadir(self):
        
        print("Añadir nuevo contacto")
        nom = input("Introduzca el nombre: ")
        telf = input("Introduzca el teléfono: ")
        email = input("Introduzca el email: ")

        self.contactos.append({'nombre': nom, 'telf': telf, 'email': email})

    def lista(self):
        
        print("Lista de contactos")
        if len(self.contactos) == 0:
            print("Ahora mismo no hay nigun contacto!")
        else:
            for contacto in self.contactos:
                print(contacto['nombre'])

    def buscar(self):
    
        print("Buscador de contactos")
        
        nom = input("Introduzca un nombre: ")

        for i in range(len(self.contactos)):
            if nom == self.contactos[i]['nombre']:
                print("Nombre:", self.contactos[i]['nombre'])
                print("Teléfono:", self.contactos[i]['telf'])
                print("Email:", self.contactos[i]['email'])
                return i

        print("Contacto no encontrado")
        return None

    def editar(self):
        
        print("Editar contacto")

        data = self.buscar()
        if data is None:
            return

        while True:
            print("1. Nombre")
            print("2. Teléfono")
            print("3. Email")
            print("4. Volver")

            opcion = int(input("Elige: "))

            if opcion == 1:
                self.contactos[data]['nombre'] = input("Nuevo nombre: ")
            elif opcion == 2:
                self.contactos[data]['telf'] = input("Nuevo teléfono: ")
            elif opcion == 3:
                self.contactos[data]['email'] = input("Nuevo email: ")
            elif opcion == 4:
                break


