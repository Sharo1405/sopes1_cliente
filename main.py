print('----------Bienvenido-----------')
#primero necesito leer ruta consola
#abrir y leer el archivo
#splitear el archivo
#hacer el balanceador
#hacer el post para el balanceador


usuarios = ['Mindy','Seen', 'Juan', 'Pedro', 'Sol', 'Luna' ,'Alex','Jose','Laura','Sharolin','Esvin', 'Andy', 'Molly', 'Rose', 'Billy', 'Andre', 'Luis', 'Ricardo', 'Anastasia', 'MAC', 'Nick', 'David', 'Lupita', 'Sharo', 'Rafael']
paraEnviar = []

opcion1 = '0'
while opcion1 == '0':
    print('Ingrese el numero de la opcion que desea ehecutar: \n ' +
          '1-Ingrese ruta \n' +
          ' 2-Ver datos \n' +
          ' 3-Enviar datos \n' +
          ' 4-SALIR \n')

    opcion = input()

    if opcion == '1':
        print('Ingresa tu ruta: ')
        ruta = input()
        archivo = open(ruta)
        textocompleto = archivo.read()
        lineas = textocompleto.split('.')
        indice = -1
        for linea in lineas:
            linea = linea.strip()
            linea = linea.replace('\n'," ")
            indice = indice + 1
            aux = ""
            aux = "{" + "\n" + "\"autor\":" + "\"" + usuarios[indice] + "\",\n" + "\"nota\": \"" + linea + "\" \n}"

            if indice == 24:
                indice = -1

            paraEnviar.append(aux)
            #print(aux)
        archivo.close()

    if opcion == '2':
        print('--------DATOS---------')
        for val in paraEnviar:
            print(val)

    if opcion == '3':
        print('---Eviando datos----')
        #aqui va el post

    if opcion == '4':
        exit()
        print('----Salio del programa----')



