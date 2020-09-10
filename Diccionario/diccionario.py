def menu():
    print('Diccionario')
    print('.......................')
    print('1. AGREGAR')
    print('2. IMPRIMIR')
    print('3. ELIMINAR')
    print('4. CONSULTAR O BUSCAR')
    print('5. SALIR')
    opcion=input('Eliga una de las opciones: ')
    return opcion

def main():
    while True:
        opcion=menu()
        
        if opcion=='1':
            print('\n'+'>>>>>AGREGAR')
            diccionario={
                'id':1006569403,
                'nombre_funcionario':'Yairinis Del Toro',
                'cargo':'Ingeniera de sistemas',
                'salario':2000000 
                }
            diccionario1={'id':"1006569404", 'nombre_funcionario2' :"elis mejia", 'cargo':"secretaria", 'salario' :"1000000" }
            
            print(diccionario,diccionario1)
            
            
            
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
          
        if  opcion=='3':
            print('\n'+'>>>>>> ELIMINAR >>>>>')
            diccionario={
                'id':1006569403,
                'nombre_funcionario':'Yairinis Del Toro',
                'cargo':'Ingeniera de sistemas',
                'salario':2000000
                }
            diccionario1={'id':"1006569404", 'nombre_funcionario2' :"elis mejia", 'cargo':"secretaria", 'salario' :"1000000" }
            diccionario2={'id':"1006566583", 'nombre_funcionario3' :"fabiana meza", 'cargo':"docente", 'salario' :"1000000" }
            diccionario2.clear()
            print(diccionario, diccionario1, diccionario2)
            print('EL FUNCONARIO HA SIDO ELIMINADO')
            
        if   opcion=='4':
            print('\n'+'>>>>>> CONSULTAR O BUSCAR >>>>>')
            diccionario={"funcionario1":{
                'id':1006569403,
                'nombre':'Yairinis Del Toro',
                'cargo':'Ingeniera de sistemas',
                'salario':2000000}
            }
            for key,value in diccionario.items():
                print(f"{key}:{value}")
            
        
            
            
            print(diccionario)
          
            print('')
            
            
        elif opcion=='5':
            print('\n'+'>>>>>> saliendo >>>>>')
            break
    return
             
            
if __name__ == '__main__':
    main()