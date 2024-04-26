import json

def abrirArchivo():
    with open(r'DIA 12\info.json', 'r') as openfile:
        return json.load(openfile)

def guardarArchivo(data):
    with open(r"DIA 12\info.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

def estudiantes(grupo):
    for estudiante in grupo["estudiantes"]:
        print("===============================")
        print("ID:", estudiante["id"])
        print("Nombre:", estudiante["nombre"])
        print("Apellido:", estudiante["apellido"])
        print("Edad:", estudiante["edad"])
        print("Fecha de Nacimiento (DD-MM-AAAA):", estudiante["fechaNacimiento"])
        print("Cédula:", estudiante["cedula"])
        print("E-mail:", estudiante["email"])
        print("GitHub:", estudiante["github"])
        print("===============================")

def modificar_estudiante(grupo):
    
    estudiante_id = int(input("Ingrese el ID del estudiante que desea modificar: "))
    for estudiante in grupo["estudiantes"]:
        if estudiante["id"] == estudiante_id:
            opcion = int(input("""
                ¿Qué desea modificar del estudiante?
                1. Apellido
                2. Nombre
                3. Edad
                4. Fecha de Nacimiento
                5. Cédula
                6. Email
                7. GitHub
                8. Eliminar estudiante
                Seleccione una opción: 
                """))
            if opcion==1:
                estudiante["apellido"] = input("Nuevo apellido: ")
                print(f'apellido')
                
            elif opcion==2:
                estudiante["nombre"] = input("Nuevo nombre: ")
                print(f'nombre')
                
            elif opcion==3:
                estudiante["edad"] = int(input("Nueva edad: "))
                print(f'edad')
                
            elif opcion==4:
                estudiante["fechaNacimiento"] = input("Nueva fecha de nacimiento (DD-MM-AAAA): ")
                print(f'fechaNacimiento')
                
            elif opcion==5:
                estudiante["cedula"] = int(input("Nueva cédula: "))
                print(f'cedula')
                
            elif opcion==6:
                estudiante["email"] = input("Nuevo email: ")
                print(f'email')
                
            elif opcion==7:
                estudiante["github"] = input("Nuevo GitHub: ")
                print(f'github')
                
            elif opcion==8:
                confirmacion=input("¿Está seguro que desea eliminar este estudiante? (S/N): ")
                if confirmacion.lower() == 's':
                    grupo["estudiantes"].remove(estudiante)
                    print("Estudiante eliminado exitosamente.")
            guardarArchivo(data)
            print("Cambio realizado.")
            return
    print("No se encontró ningún estudiante con ese ID.")

def menu_principal(data):
    while True:
        print("============================")
        print("       MENU DE GESTION      ")
        print("============================")
        print("1. Revisar estudiantes")
        print("2. Modificar estudiante")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            for grupo in data:
                print("Grupo:", grupo["grupo"])
                estudiantes(grupo)
                
        elif opcion == "2":
            for grupo in data:
                print("Grupo:", grupo["grupo"])
                modificar_estudiante(grupo)
                
        elif opcion == "3":
            print("Gracias por usar el programa")
            break
        
        else:
            print("Opción inválida.")

data = abrirArchivo()
menu_principal(data)

#Creado por Miguel Guerrero C.C 1090381839