#Patricio Carrasco
print("aplicacion de salud")

estimulo = input(" el paciente responde a estimulos? (SI) (NO): ").lower()
si = "SI"
no = "NO"

if estimulo == 'si':
    print("llevelo al hospital mas cercano")
elif estimulo == "no":
    print("abrir las vias respiratorias")
    estimulo2 = input("el paciente respira? (SI) (NO): ").lower()
    if estimulo2 == "si":
        print("permitirle posicion de suficiente ventilacion")
    elif estimulo2 == "no":
        print("Administrar 5 ventilaciones y llamar ambulancia")
        estimulo3 = input("el paciente tiene signos de vida? (SI) (NO): ").lower()
        while estimulo3 != "si":
            print("administrar compresiones hasta que llegue la ambulancia")
            estimulo4 = input(" llego la ambulancia? (SI)  (NO): ").lower()
            if estimulo4 =="si":
                print("adios")
                break
            elif estimulo4=="no":
                print("administrar compresiones hasta que llegue la ambulancia")
            estimulo3 = input("el paciente tiene signos de vida? (SI) (NO): ").lower()
        print("llego la ambulancia")
