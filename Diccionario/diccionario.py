def menu():
    print('Diccionario')
    print('.......................')
    print('1. AGREGAR')
    print('2. IMPRIMIR')
    print('5. SALIR')
    opcion=input('Eliga una de las opciones: ')
    return opcion

def main():
    while True:
        opcion=menu()
        
        if opcion=='1':
            print('\n'+'>>>>>AGREGAR')
            funcionarios={
                "funcionario1":{ 
                'id':1006569403,
                'nombre_funcionario':'Yairinis Del Toro',
                'cargo':'Ingeniera de sistemas',
                'salario':2000000 
                },
            "funcionario2":{'id':"1006569404", 'nombre_funcionario2' :"elis mejia", 'cargo':"secretaria", 'salario' :"1000000" },
            "funcionario3":{'id':"1006569404", 'nombre_funcionario3' :"luisa marta", 'cargo':"administradora", 'salario' :"1000000" }
            }
            print(funcionarios)    
            
        if opcion=='2':
            print('\n'+'>>>>>> IMPRIMIR >>>>>')
            diccionario={
                'id':1006569403,
                'nombre_funcionario':'Yairinis Del Toro',
                'cargo':'Ingeniera de sistemas',
                'salario':2000000
                }
            print(diccionario)
            print('')
          
        
        elif opcion=='5':
            print('\n'+'>>>>>> saliendo >>>>>')
            break
    return
             
            
if __name__ == '__main__':
    main()