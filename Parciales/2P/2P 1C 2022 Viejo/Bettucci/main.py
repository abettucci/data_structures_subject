import csv 
import validaciondeImpresiones as vld
import time
import matplotlib.pylab as plt

ventas={}
id=set()
eleccion=vld.menu()
while eleccion!=12:
    if eleccion==1:
        start= time.process_time()
        direccion=input("Ingrese el path de el csv que quiere agregar: ")
        with open(direccion, "r") as csvfile:
            columnas=tuple(["Invoice ID","Branch","City","Customer type","Gender","Product line","Unit price","Quantity","Tax 5%","Total","Date","Time","Payment","cogs","gross margin percentage","gross income","Rating"])
            reader=csv.DictReader(csvfile, fieldnames=columnas,delimiter=";")
            for row in reader:
                ventas[row["Invoice ID"]]={"Branch": row["Branch"],"City":row["City"],"Customer type" : row["Customer type"],"Gender": row["Gender"],"Product line":row["Product line"], "Unit price": row["Unit price"],"Quantity": row["Quantity"],"Tax 5%": row["Tax 5%"],"Total":row["Total"],"Date": row["Date"],"Time": row["Time"],"Payment": row["Payment"],"cogs":row["cogs"],"gross margin percentage": row["gross margin percentage"],"gross income":row["gross income"],"Rating":row["Rating"]}
        Final=time.process_time()-start
    elif eleccion==2:
        start= time.process_time()
        id=input("Ingrese el id: ")
        while(id in ventas.keys()):
            id=input("Ingrese el id: ")
        ventas[id]={"Branch":"A","City":"Yangon","Customer type":"Member","Gender":"Female","Product line":"Health and beauty","Unit price":74.69,"Quantity":7,"Tax 5 %":26.1415,"Total":548.9715,"Date":1/5/2019,"Time":"13:08","Payment":"Ewallet","cogs":522.83,"gross margin percentage":4.761904762,"gross income":26.1415,"Rating":9.1}
        Final=time.process_time()-start
    elif eleccion==3:
        start= time.process_time()
        AvgRatEwallet=0
        CantEwallet=0
        AvgRatOtros=0 #junto cash y credit card
        CantOtros=0
        for key in ventas.keys():
            if ventas[key]["Payment"]=="Ewallet":
                CantEwallet+=1
                AvgRatEwallet+=float(ventas[key]["Rating"])
            else:
                CantOtros+=1
                AvgRatOtros+=float(ventas[key]["Rating"])
        if(AvgRatEwallet/CantEwallet<AvgRatOtros/CantOtros):
            print("Pagar con Ewallet no mejora el rating de la compra.")
        else:
            print("Pagar con Ewallet mejora el rating de la compra")
        Final=time.process_time()-start
    elif eleccion==4: #calculo el ingreso de cada genero y luego el porcentaje sobre la (suma de ambos=totalposta)
        start= time.process_time()
        IngresoHombres=0
        IngresoMujeres=0
        for key in ventas.keys():
            if ventas[key]["Gender"]=="Female":
                IngresoMujeres+=float(ventas[key]["Total"])
            elif ventas[key]["Gender"]=="Male":
                IngresoHombres+=float(ventas[key]["Total"])
        porcentajeHombres=round(IngresoHombres/(IngresoHombres + IngresoMujeres) * 100, 2)
        porcentajeMujeres=round(IngresoMujeres/(IngresoHombres + IngresoMujeres) * 100,2)
        print("El porcentaje de ingresos por venta de hombre es de %",porcentajeHombres)
        print("El porcentaje de ingresos por venta de mujeres es de %",porcentajeMujeres)
        Final=time.process_time()-start
    elif eleccion==5:
        start=time.process_time()
        calYangon=0
        calNaypyitaw=0
        calMandalay=0
        cantYangon=0
        cantNaypyitaw=0
        cantMandalay=0
        for key in ventas.keys():
            if ventas[key]["City"]==["Yangon"]:
                calYangon+=float(ventas[key]["Rating"])
                cantYangon+=1
            elif ventas[key]["City"]=="Naypyitaw":
                calNaypyitaw+=float(ventas[key]["Rating"])
                cantNaypyitaw+=1
            elif ventas[key]["City"]=="Mandalay":
                calMandalay+=float(ventas[key]["Rating"])
                cantMandalay+=1
        
        yangon=calYangon/cantYangon
        naypyitaw=calNaypyitaw/cantNaypyitaw
        mandalay=calMandalay/cantMandalay
        if(yangon>naypyitaw):
            if(yangon>mandalay):
                sucursal="yangon"
            else:
                sucursal="mandalay"
        elif(naypyitaw>mandalay):
            sucursal="naypyitaw"
        else:
            sucursal="mandalay"
        print("La sucursal mejor calificada por los clientes es la de", sucursal)
        Final=time.process_time()-start
    elif eleccion==6:
        start=time.process_time()
        diccionario={"Yangon": [0,0], "Naypyitaw": [0,0], "Mandalay": [0,0]} #el primero es member y el segundo normal
        for key in ventas.keys():
            if ventas[key]["Customer type"]=="Member":
                diccionario[ventas[key]["City"]][0]+= float(ventas[key]["Total"])
            elif ventas[key]["Customer type"]=="Normal":
                diccionario[ventas[key]["City"]][1]+= float(ventas[key]["Total"])
        for key in diccionario.keys():
            if(diccionario[key][0]<diccionario[key][1]):
                print("Para la ciudad {}, los normales gastaron más que los members".format(key))
            else:
                print("Para la ciudad {}, los members gastaron más que los normales".format(key))
        Final=time.process_time()-start
    elif eleccion==7:
        start=time.process_time()
        productos={"Health and Beauty":[0.0,0.0],"Electronic Accesories":[0.0,0.0],"Home and Lifestyle":[0.0,0.0],"Sports and Travel":[0.0,0.0]}#el primero es el rating y el segundo la cantidad
        for key in ventas.keys():
            if ventas[key]["Product Line"]=="Health and Beauty":
                productos[ventas[key]["Product Line"]][0]+= float(ventas[key]["Rating"])
                productos[ventas[key]["Product Line"]][1]+= float(ventas[key]["Quantity"])
            elif ventas[key]["Product Line"]=="Electronic Accesories":
                productos[ventas[key]["Product Line"]][0]+= float(ventas[key]["Rating"])
                productos[ventas[key]["Product Line"]][1]+= float(ventas[key]["Quantity"])
            elif ventas[key]["Product Line"]=="Home and Lifestyle":
                productos[ventas[key]["Product Line"]][0]+= float(ventas[key]["Rating"])
                productos[ventas[key]["Product Line"]][1]+= float(ventas[key]["Quantity"])
            elif ventas[key]["Product Line"]=="Sports and Travel":
                productos[ventas[key]["Product Line"]][0]+= float(ventas[key]["Rating"])
                productos[ventas[key]["Product Line"]][1]+= float(ventas[key]["Quantity"])
        myList = productos.items()
        myList = sorted(myList)
        x, y = zip(*myList)
        plt.plot(x, y)
        plt.xlabel('Key')
        plt.ylabel('Value')
        plt.title('Grafico de relacion de Rating y Cantidad de producto')
        plt.show()
        Final=time.process_time()-start
    elif eleccion==8:
        start=time.process_time()
        porcentajeHombres
        porcentajeMujeres
        sexo=["female","men"]
        porcentajes=[porcentajeMujeres,porcentajeHombres]
        plt.pie(porcentajes,labels=sexo,autopct="%1.2f%%")
        plt.title(label="Porcentaje de ingresos segun el genero",loc="center",color="pink")
        plt.show()
        Final=time.process_time()-start
    elif eleccion==9:
        start=time.process_time()
        date=input("Ingrese una fecha: ")
        hour=input("Ingrese una hora: ")
        date=vld.transformacionFecha(date)
        hour=vld.transformacionHora(hour)
        for key in ventas.keys():
            if(int(vld.transformacionFecha(ventas[key]["Date"])[2])>int(date[2])):
                print(ventas[key],end="\n")
            elif(int(vld.transformacionFecha(ventas[key]["Date"])[2])==int(date[2])):
                if(int(vld.transformacionFecha(ventas[key]["Date"])[0])>int(date[0])):
                    print(ventas[key],end="\n")
                elif(int(vld.transformacionFecha(ventas[key]["Date"])[0])==int(date[0])):
                    if(int(vld.transformacionFecha(ventas[key]["Date"])[1])>int(date[1])):
                        print(ventas[key],end="\n")
                    elif(int(vld.transformacionFecha(ventas[key]["Date"])[1])==int(date[1])):
                        if(int(vld.transformacionHora(ventas[key]["Time"])[0])>int(hour[0])):
                            print(ventas[key],end="\n")
                        elif(int(vld.transformacionHora(ventas[key]["Time"])[0])==int(hour[0])):
                            if(int(vld.transformacionHora(ventas[key]["Time"])[1])>int(hour[1])):
                                print(ventas[key],end="\n")
        Final=time.process_time()-start
    elif eleccion==10:
        start= time.process_time()
        date=input("Ingrese una fecha: ")
        hour=input("Ingrese una hora: ")
        date=vld.transformacionFecha(date)
        hour=vld.transformacionHora(hour)
        for key in ventas.keys():
            if(int(vld.transformacionFecha(ventas[key]["Date"])[2])<int(date[2])):
                print(ventas[key],end="\n")
            elif(int(vld.transformacionFecha(ventas[key]["Date"])[2])==int(date[2])):
                if(int(vld.transformacionFecha(ventas[key]["Date"])[0])<int(date[0])):
                    print(ventas[key],end="\n")
                elif(int(vld.transformacionFecha(ventas[key]["Date"])[0])==int(date[0])):
                    if(int(vld.transformacionFecha(ventas[key]["Date"])[1])<int(date[1])):
                        print(ventas[key],end="\n")
                    elif(int(vld.transformacionFecha(ventas[key]["Date"])[1])==int(date[1])):
                        if(int(vld.transformacionHora(ventas[key]["Time"])[0])<int(hour[0])):
                            print(ventas[key],end="\n")
                        elif(int(vld.transformacionHora(ventas[key]["Time"])[0])==int(hour[0])):
                            if(int(vld.transformacionHora(ventas[key]["Time"])[1])<int(hour[1])):
                                print(ventas[key],end="\n")
        Final=time.process_time()-start
    elif eleccion==11:
        start= time.process_time()
        listaVentas=[]
        for key, row in ventas.items():
            listaVentas.append([key, row["Branch"],row["City"], row["Customer type"], row["Gender"],row["Product line"], row["Unit price"],row["Quantity"], row["Tax 5%"], row["Total"],row["Date"],row["Time"],row["Payment"],row["cogs"], row["gross margin percentage"],row["gross income"],row["Rating"]])
        listaVentas.sort(key= lambda x: (vld.valorNumericofechaHora(x[10], x[11])))
        print(listaVentas)
        Final=time.process_time()-start
    elif eleccion == 12:
        start= time.process_time()
        listaVentas=[]
        for key, row in ventas.items():
            listaVentas.append([key, row["Branch"],row["City"], row["Customer type"], row["Gender"],row["Product line"], row["Unit price"],row["Quantity"], row["Tax 5%"], row["Total"],row["Date"],row["Time"],row["Payment"],row["cogs"], row["gross margin percentage"],row["gross income"],row["Rating"]])
        listaVentas.sort(key= lambda x: (vld.valorNumericofechaHora(x[10], x[11])), reverse=False)
        print(listaVentas)
        Final=time.process_time()-start

    print("\nTiempo utilizado:", Final, "\n")
    
    
    eleccion=vld.menu()    
        
                
                
        

        


        
        
        
        
        
        
    
