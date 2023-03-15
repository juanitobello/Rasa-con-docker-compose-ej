#TODO: importanciones para Json Arcgis
import json
import requests

#TODO: Importanciones para XML
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as  ET
import pandas as pd

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
    endpoint= "http://ide.ucuenca.edu.ec/api/igo2/createTemporalViwer"
    # Convertir los datos en formato JSON
    json_datos= json.dumps(datos)
    # # Encabezados de la solicitud
    headers = {"Content-Type": "application/json"}
    # # Hacer la solicitud POST y obtener la respuesta
    response = requests.post(endpoint, data=json_datos, headers=headers, verify= False)
    # # Imprimir la respuesta
    print(response.text)

    
def addinfDatos(tittle, url, tipo, layer):
    a={
        "title": tittle,
        "baseLayer": False,
        "visible": False,
        "type": tipo,
        "url": url,
        "layers": layer,
        "version": "1.3.2",
        "queryable":True,
      }
    datos.append(a)

#Para buscar dentro del dataframe
def funDinamicQuerry(intencion):
    df= pd.read_csv('base.csv')
    df.dropna()
    #print(df.head())
    df2=df[df.subeje.str.contains(pat=intencion,na=False, case=False)]
    df3=df2[['Titulo Capa', 'Enlace servicio', 'Nombre Capa', 'Identificador', 'Tipo']]
    print("Lo nuevo:"+str(len(df3)))
    
    #Para recrrer el data frame resultante 
    for indice, fila in df3.iterrows():
        addinfDatos(fila['Titulo Capa'], fila['Enlace servicio'], fila['Tipo'], fila['Nombre Capa'])
    
    
#Para comprobar que se crearon correctaente los json
    print(len(datos))
    with open(r'export_data.json', 'w') as fp:
        json.dump(datos, fp, indent=4)
    
    
    
    createVisor(datos)
    print('Se creo el mapa')
    del datos[2:len(datos)]
    print(len(datos))
    
    
funDinamicQuerry("redes_hidrograficas")