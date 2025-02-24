try:
    medio=input('ingrese el medio de pago que desea buscar')
    with open('SalesJan2009.csv', 'r', encoding='utf-8') as f:
        total_compras=0
        for line in f:
            if medio in line:
                total_compras+=1                 
        print(total_compras)
        if total_compras==0:
            print('no hay compras con este medio')                
except FileNotFoundError:
    print(f"El archivo 'SalesJan2009.csv' no se encontró.")
