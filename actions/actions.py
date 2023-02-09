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
