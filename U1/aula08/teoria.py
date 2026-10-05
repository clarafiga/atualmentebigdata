#saint graal  - set / list / tuple / dict

def calculadora1 ():    
num1 = float(input( "digite"))
num2 = float(input("digite mais um"))

operador = input("Informe a ope : 1. adição ; 2. subtração ; 3. multiplica & 4.divisao")

match operador:
    case "1":
        print(f"Resultado:{num1+num2}")
    case "2":
        print (f"Resultado:{num1+num2}")
    case "3":
        print (f"Resultado:{num1+num2}")
    case "4":
        if num2 !=0:
            print (f"Resultado:{num1+num2}")
        else:
            print(f"Burro")
    