# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []


import json
import requests

#TODO: Importanciones para XML
import urllib.parse, urllib.error
import xml.etree.ElementTree as  ET
import pandas as pd

#imports to custom actions
import webbrowser


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

def openLink():
    webbrowser.open('https://google.com',  new=1, autoraise=True)

def openRicaurte():
    webbrowser.open('https://ide.ucuenca.edu.ec/geoportal/viwer/3?context=3&zoom=13&center=-78.98518,-2.87754&invisiblelayers=*&visiblelayers=89053566f0abfa20b936f539b27066bd,OSM',  new=1, autoraise=True)

def openPostes():
    webbrowser.open('https://ide.ucuenca.edu.ec/geoportal/viwer/1?context=1&zoom=16&center=-79.01005,-2.90492&invisiblelayers=*&visiblelayers=508b5791b7ff3809f103bc57e1b50970,OSM',  new=1, autoraise=True)


#Clases de Rasa
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hola Juan")

        return []


class ActionButtonsSiNo(Action):

    def name(self) -> Text:
        return "action_buttons_sino"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ops=[
            {"payload":'/affirmacion', "title": "Sí"},
            {"payload":'/int_saltar', "title": "Saltar"},
        ]

        dispatcher.utter_message(text="Bienvenido! ¿Deseas más instrucciones?", buttons=ops)

        return []




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
    
    
#funDinamicQuerry("redes_hidrograficas")

#Open indes
class ActionOpenIndex(Action):

    def name(self) -> Text:
        return "action_open_index"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Redirigiendo...")
        dispatcher.utter_message(text='[Curso AV IDE](https://ide.ucuenca.edu.ec/?p=412)')
        openLink()
        return []

#Open Ricaurte
class ActionOpenRicaurte(Action):

    def name(self) -> Text:
        return "action_open_ricaurte"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Redirigiendo a Visor 1")        
        dispatcher.utter_message(text="Click aqui para ver resultado: [construcciones Ricaurte](https://ide.ucuenca.edu.ec/geoportal/viwer/3?context=3&zoom=13&center=-78.98518,-2.87754&invisiblelayers=*&visiblelayers=89053566f0abfa20b936f539b27066bd,OSM)")        
        #openRicaurte()
        return []

#Open Postes
class ActionOpenPostes(Action):

    def name(self) -> Text:
        return "action_open_postes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Redirigiendo a Visor 2")
        dispatcher.utter_message(text="Click aqui para ver resultado: [capa transdistribucion](https://ide.ucuenca.edu.ec/geoportal/viwer/1?context=1&zoom=16&center=-79.01005,-2.90492&invisiblelayers=*&visiblelayers=508b5791b7ff3809f103bc57e1b50970,OSM)")        
        #openPostes()
        return []
    

#Open Postes
class ActionSayausi(Action):

    def name(self) -> Text:
        return "action_sayausi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Cargando Visor 2")
        dispatcher.utter_message(text="Click aqui para ver resultado: [Resultado Sayausi](https://ide.ucuenca.edu.ec/geoportal/viwer/2?context=2&zoom=15&center=-79.07272,-2.87452&invisiblelayers=*&visiblelayers=c87a54091a46f9f560975bca3d5bd4eb,22baf1087c32ec231faf06aae2574b51,OSM)")        
        return []


class ActionSanJoaquin(Action):

    def name(self) -> Text:
        return "action_sanjoaquin"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Cargando Visor 2")
        dispatcher.utter_message(text="Click aqui para ver resultado: [Resultado San Joaquin](https://ide.ucuenca.edu.ec/geoportal/viwer/2?context=2&zoom=15&center=-79.05164,-2.8938&invisiblelayers=*&visiblelayers=d0fdca5f9279b7d97497ad298f0ed750,OSM)")        
        return []
    
#Action redes_hidrograficas
class Actionredes_hidrograficas(Action):
	def name(self) -> Text:
		return "action_redes_hidrograficas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
                
		dispatcher.utter_message(text="Creando Visor")
		dispatcher.utter_message(text="Click aqui para ver resultado: [redes_hidrograficas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
        
		funDinamicQuerry("redes_hidrograficas")
		return []



#Actions para 4 votones
class ActionButtons(Action):

    def name(self) -> Text:
        return "action_buttons"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons=[
            {"payload":'/int_movimiento_de_tierra{"tipo_emergencia":"movimientos"}', "title": "Movimientos en Masa"},
            {"payload":'/int_deslizamiento{"tipo_emergencia":"deslizamientos"}', "title": "Deslizamientos"},
            {"payload":'/int_inundaciones{"tipo_emergencia":"inundaciones"}', "title": "Inundaciones"},
            {"payload":'/int_volcanes"{"tipo_emergencia":"volcanes"}', "title": "Volcanes"},
        ]
        dispatcher.utter_message(text="Escoge un ítem para mostrar en el mapa:", buttons=buttons)
        #dispatcher.utter_message(text="http://localhost:4200/?context=igm_geopedologia&zoom=14&center=-78.51865,-0.22732&visiblelayers=*&invisiblelayers=a24677c2b5530b3e04f38f091dfae324,fond_osm_hot", buttons=buttons)

        return []
