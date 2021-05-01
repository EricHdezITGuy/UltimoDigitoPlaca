"""
Realice un programa que lea el último dígito de la placa y 
determine los días de no circulación durante todo el día y 
los días en que no puede circular libremente los fines de semana.

"""

digito = int(input("Ultimo dígito de la placa->"))

if digito >=0 and digito <=9:
    if digito==1 or digito==2:
        restricSemana = "Lunes"
    elif digito==3 or digito==4:
        restricSemana = "Martes"
    elif digito==5 or digito==6:
        restricSemana = "Miércoles"
    elif digito==7 or digito==8:
        restricSemana = "Jueves"
    else:
        restricSemana = "Viernes"
else:
    print("ERROR: El número digitado no corresponde a un digito")
    
if digito % 2 == 0:
    restricFinSem = "Sábado"
else:
    restricFinSem = "Domingo"
    
print ("Días de restriccion: ", restricSemana , " y " , restricFinSem)






