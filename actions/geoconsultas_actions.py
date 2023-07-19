# -*- coding: utf-8 -*-
"""
Created on Wed MAR  7 16:17:44 2023

@author: juan francisco Bustamante
"""

#TODO: importanciones para Json Arcgis
import json
import requests

#TODO: Importanciones para XML
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as  ET
import pandas as pd

location="place"
xmin= 737423.25
ymin= 691969.0
xmax= 741381.5625
ymax= 9699106.0
epsg= 32717

listawms=[
    'https://www.geoportaligm.gob.ec/p_geoinformacion/Cobertura_Uso/wms?',
    'https://www.geoportaligm.gob.ec/p_geoinformacion/Geopedologia/wms?',
    'https://www.geoportaligm.gob.ec/p_geoinformacion/Geomorfologia/wms?',
    'https://www.geoportaligm.gob.ec/p_geoinformacion/AreasNaturales/wms?',
    'https://www.geoportaligm.gob.ec/p_geoinformacion/PANE_CoberturaUso/wms?',
    'https://www.geoportaligm.gob.ec/p_geoinformacion/PANE_Geopedologia/wms?',
    'https://www.geoportaligm.gob.ec/p_geoinformacion/PANE_CUT/wms?',
    'http://ide.cuenca.gob.ec/geoserver/ide/wms?',
    'http://ide.cuenca.gob.ec/geoserver/prueba/wms?',
    'http://ide.cuenca.gob.ec/geoserver/ide_interno/wms?',
    'https://gis.uazuay.edu.ec/geoserver/dron_multiespectrales/wms?',
    'https://gis.uazuay.edu.ec/geoserver/VisorSenplades/wms?',
    'https://gis.uazuay.edu.ec/geoserver/CEPRA/wms?',
    'https://gis.uazuay.edu.ec/geoserver/PlanificacionTerritorial/wms?',
    'https://gis.uazuay.edu.ec/geoserver/inventario_forestal/wms?',
    'https://gis.uazuay.edu.ec/geoserver/azuay_250k/wms?',
    'https://gis.uazuay.edu.ec/geoserver/emac/wms?',
    'https://gis.uazuay.edu.ec/geoserver/azuay_50k/wms?',
    'https://gis.uazuay.edu.ec/geoserver/ortofotos_drone/wms?',
    'https://gis.uazuay.edu.ec/geoserver/calidad_ambiental/wms?',
    'https://gis.uazuay.edu.ec/geoserver/riesgos_cuenca/wms?',
    'https://gis.uazuay.edu.ec/geoserver/cobertura_vegetal_5k/wms?',
    'https://gis.uazuay.edu.ec/geoserver/parques_cuenca/wms?',
    'https://geoinec.inec.gob.ec/geoinec/inec/wms?',
        ]

listaArcGis=[
    #'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Catastro_Redes_de_Agua_Potable_y_Alcantarillado/FeatureServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Catastro_Redes_de_Agua_Potable_y_Alcantarillado/MapServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Ecuador_provincias/MapServer',
    #'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Establecimientos_Recoleccion_Desechos/FeatureServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Establecimientos_Recoleccion_Desechos/MapServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/estaciones_sga/MapServer',
    #'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Levantamientos/FeatureServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Levantamientos/MapServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Locales_Recaudacion/MapServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Parroquias/MapServer',
    #'https://geo.etapa.net.ec/arcgis/rest/services/Publico/puntos_wifi/FeatureServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/puntos_wifi/MapServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Referencias_General/MapServer',
    'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Visor_Telecom/MapServer',
    'https://geoservicios2.centrosur.gob.ec/geoservicios/rest/services/Geoportal_Publico/GeopPublic_RedesDist_rsgis1/MapServer',
]




# class layer():
#     def __init__(self, title, baseLayer, visible, type,url, layers, version,queryable):
#         self.title = title
#         self.baseLayer = baseLayer
#         self.visible = visible
#         self.type = type
#         self.url = url
#         self.layers = layers
#         self.version = version
#         self.queryable = queryable


# class sourceOptions():
#     def __init__(self, type, url, maxZoom, params, queryable):
#         self.type = type
#         self.url = url
#         self.maxZoom = maxZoom
#         self.params = params #object params inside sourceOptios
#         self.queryable = queryable

# class params():
#     def __init__(self, layers, version):
#         self.layers = layers
#         self.version = version 


# #TODO: Codigo para WMS con XML
# url = 'https://gis.uazuay.edu.ec/geoserver/cobertura_vegetal_5k/wms?request=getcapabilities'
# uh =  urllib.request.urlopen(url)
# data = uh.read()

# projection = "ricaurte"
 
# print("uh es tipo: ",type(uh))

# print("data es tipo: ", type(data))


# if projection in str(data):
#     print("Contains")
# else:
#     print("Contains not")

# #for w in range(5):
# for w in listawms:
#     url=str(w)+"request=getcapabilities"
#     uh=urllib.request.urlopen(url)

    
# #TODO: Codigo para Arcgis con JSON
# url_base= 'https://geo.etapa.net.ec/arcgis/rest/services/Publico/Visor_Telecom/MapServer?f=json'
# response= urllib.request.urlopen(url_base)
# jsonData= json.loads(response.read())
# print('\nEl tipo de jsonData:::::',type(jsonData))
# var = input('Ingrese el nombre de la capa que desea buscar: ')
# for i in jsonData['layers']:
#     if i['name'] == var:
#         print('EL ID de la capa es: ',i['id'])




# def createListLayers():
#     listLayers = []
#     title = "Capa de prueba 2"
#     baseLayer = False
#     visible = False
#     type = "wms"
#     url ="https://www.geoportaligm.gob.ec/p_geoinformacion/Cobertura_Uso/wms?"
#     layers = "m_sistemasprod_homologado_a"
#     version = "1.3.2"
#     queryable = True

#     for i in range(4):
#         listLayers.append(layer(title, baseLayer,visible,type,url, layers,version,queryable))

#     return listLayers
    

# print('tamaño de la lista '+ str(len(createListLayers())))


# listLayers = createListLayers()
# jsonString = json.dumps(listLayers, default = lambda x: x.__dict__) #TODO: para crear lista de obj to json
# print(jsonString)



##########------------------------ Programación para ver si las capas estan en el la area seleccionada --------------------------------###########
def getCoordenadas():
    # URL del microservicio
    url = "https://ide.ucuenca.edu.ec/api/parroquia/checkLayerWithinIntersectPlace/nombre_parroquia"
    # Formato JSON que se enviará en la solicitud GET
    data = [
      {
        "id": 1,
        "name": "Cuenca",
        "xmin": -79.0752944946289,
        "ymin": -2.96273040771484,
        "xmax": -78.9155197143555,
        "ymax": -2.83643651008606,
        "epsg": 32717
      },
      {
        "id": 2,
        "name": location,
        "xmin": xmin,
        "ymin": ymin,
        "xmax": xmax,
        "ymax": ymax,
        "epsg": 32717
      }
    ]
    
    # Convertir los datos en formato JSON
    json_data = json.dumps(data)
    
    # Encabezados de la solicitud
    headers = {"Content-Type": "application/json"}
    
    # Hacer la solicitud GET y obtener la respuesta
    response = requests.get(url, data=json_data, headers=headers, verify= False)
    
    # Imprimir la respuesta
    print(response.text)





###__------------- Codigo Para crear visor y cagar capas-----------------#####

datos= [
#Mandar estos dos primeros directamente a la lista
    {
        "title": "Open Street Map - Humanitaire",
        "baseLayer": True,
        "visible": False,
        "type": "osm",
        "url": "https://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png",
        "maxZoom": 19,
        "optionsFromCapabilities": True,
        "params": {}

    },
    {
        "title": "Open Street Map",
        "baseLayer": True,
        "visible": True,
        "type": "osm",
        "url": "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        "maxZoom": 19,
        "optionsFromCapabilities": True,
        "params": {}

    }
]

def createVisor(datos):
    endpoint= "https://201.159.220.172/api/igo2/createTemporalViwer"
    #endpoint= "https://172.17.0.1/api/igo2/createTemporalViwer"
    # Convertir los datos en formato JSON
    json_datos= json.dumps(datos)
    # # Encabezados de la solicitud
    headers = {"Content-Type": "application/json"}
    # # Hacer la solicitud POST y obtener la respuesta
    response = requests.post(endpoint, data=json_datos, headers=headers, verify= False)
    # # Imprimir la respuesta
    print("RESPUESTA DEL VISOR DE MAPAS:")
    #print(response.text)

    
def addinfDatos(tittle, url, tipo, layer):
    a={
        "title": tittle,
        "baseLayer": False,
        "visible": True,
        "type": tipo,
        "url": url,
        "layers": layer,
        "version": "1.3.2",
        "queryable":True,
        "optionsFromCapabilities": True,
      }
    datos.append(a)

#Para buscar dentro del dataframe
def funDinamicQuerry(intencion):
    intencion= intencion.replace("_", " ")
    df= pd.read_csv("actions/Base_de_Conocimiento_actions.csv")
    #df= pd.read_csv("./Base_de_Conocimiento_actions.csv")
#     url = "https://ide.ucuenca.edu.ec/api/basededatosespacial/capas"
#     response = requests.get(url)

# # Verificar si la solicitud fue exitosa
#     if response.status_code == 200:
#     # Obtener los registros de la respuesta JSON
#         df = response.json()
    df.dropna()
    #print(df.head())
    df2=df[df.subeje.str.contains(pat=intencion,na=False, case=False)]
    df3=df2[['Organizacion','Titulo Capa', 'Enlace servicio', 'Nombre Capa', 'Identificador', 'Tipo', "Eje Pertenece"]]
    print("Coincidencias con subeje: "+str(len(df3)))
    #print(df3.head())
    
    #Para recrrer el data frame resultante 
    for indice, fila in df3.iterrows():
        addinfDatos(fila['Identificador'], fila['Enlace servicio'], fila['Tipo'], fila['Nombre Capa'])
    
#Para comprobar que se crearon correctaente los json
    print("Lista a enviar subeje + 2="+str(len(datos)))
    with open(r'export_data.json', 'w') as fp:
        json.dump(datos, fp, indent=4)
    
#Extraer EJE pertence
    eje_pertenece=df3.iloc[0,6]    
    print("corrdenadas xmin, ymin, xmax, ymax, epsg, null")    
    valores_unicos = df3['Organizacion'].unique()
    valores_cadena = ', '.join(map(str, valores_unicos))
    eje_insticion= eje_pertenece + "\n\nCapas encontradas: "+str(len(df3))+"\nRecuperando información de: " + valores_cadena
    print(eje_insticion)
#crear vision
    createVisor(datos)
    print('Se creo el mapa')
    del datos[2:len(datos)]
    print("Limpio "+str(len(datos)))
    
    return eje_insticion
    
#funDinamicQuerry("actividades_economicas")
#funDinamicQuerry("redes hidrograficas")
#funDinamicQuerry("parques")
#funDinamicQuerry("ductos")
funDinamicQuerry("imagen satelital")