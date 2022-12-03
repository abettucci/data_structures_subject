# class Camion():
#     def __init__(self, patente,carga,marca, año):
#         self.patente=patente
#         self.carga = carga
#         self.marca=marca
#         self.año=año
#     def __eq__(self, otro):
#         return self.carga==otro.carga and self.año==otro.año and self.patente==otro.patente
#     def __str__(self):
#         return('El camion de patente {}, marca {} y año {}, carga {} toneladas mensuales'.format(self.patente,
#         self.marca,self.año,self.carga))

# furgon1=Camion('HPP 321',450,'Ford',2000)
# furgon2=Camion('HP 221',700,'IVECO',2013)
# furgon3=Camion('HP 221',700,'IVECO',2013)
# print(furgon1==furgon2)
# print(furgon3==furgon2)

class Camion():
    def __init__(self):
        self.patente= input('Ingrese patente del camion: ')
        self.carga = int(input('Ingrese carga del camion: '))
        self.marca= input('Ingrese marca del camion: ')
        self.año= int(input('Ingrese año del camion: '))
    def __eq__(self, otro):
        return self.carga==otro.carga and self.año==otro.año and self.patente==otro.patente
    def __str__(self):
        return('El camion de patente {}, marca {} y año {}, carga {} toneladas mensuales'.format(self.patente,
        self.marca,self.año,self.carga))

#furgon1=Camion()
#print(furgon1)
# furgon2=Camion()
# print(furgon2)
# furgon3=Camion()
# print(furgon3)

# print(furgon1==furgon2)
# print(furgon3==furgon2)

