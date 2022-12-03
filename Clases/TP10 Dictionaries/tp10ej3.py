'''
Escriba una función que dado un conjunto de diccionarios (clave: string, contenido: real) 
devuelva un único diccionario (clave: string, valor conjunto de reales).'''


conjuntoDic = ({'Pan': 22.8,'Pollo': 33.85},
    {'Mermerlada': 42.5, 'Pan': 23.55, 'Tomate': 18.3},
    {'Pan': 28.0, 'Tomate': 19.5, 'Pollo': 34.6}
)

dict1 = conjuntoDic[0]
dict2 = conjuntoDic[1]
dict3 = conjuntoDic[2]

def unificarDiccionarios(dict1, dict2,dict3):
    return {
        k: list(d[k] for d in (dict1,dict2,dict3) if k in d)
        # con d[k] obtengo el valor del alimento dado (k) en cada uno de los diccionarios
        for k in set(dict1.keys()) | set(dict2.keys()) | set(dict3.keys()) # el | significa "or"
        #me fijo si el alimento se encuentra en la lista de alimentos (que estan en un set) de cada uno de los diccionarios
        #estoy devolviendo una lista con los valores de cada alimento, deberia cambiarlo para que sea un diccionario con los valores de cada alimento
    }
print(unificarDiccionarios(dict1,dict2,dict3))

