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
import actions.geoconsultas_actions as geo

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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

        dispatcher.utter_message(text="¿Deseas más instrucciones?", buttons=ops)

        return []


#Open indes
class ActionOpenIndex(Action):

    def name(self) -> Text:
        return "action_open_index"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Aquí tienes página principal del [Proyecto AV-PPGIS](https://ide.ucuenca.edu.ec/?page_id=147)")
        dispatcher.utter_message(text='Aquí tienes un curso de capación en IDEs [Curso AV IDE UCuenca](https://educacionvirtual.cedia.edu.ec/courses/course-v1:CEDIA+UC-BD-001+2023_T1/about)')
        return []

class ActionFarmacias(Action):

    def name(self) -> Text:
        return "action_farmacias"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Creando Visor")
        dispatcher.utter_message(text="Click aqui para ver resultado: [farmacias](https://ide.ucuenca.edu.ec/geoportal/viwer/1?context=1&zoom=14&center=-79.01062,-2.90174&invisiblelayers=*&visiblelayers=8217eaa5cbaf389ac0d54f057b781b2d,c215566667686f2ed7b81702e4aae9ed,OSM)")
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

class ActionRedesHidrograficas(Action):

    def name(self) -> Text:
        return "action_redes_hidrograficas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        eje_pertenece = geo.funDinamicQuerry("redes_hidrograficas")
        dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
        dispatcher.utter_message(text="Click aqui para ver resultado: [redes_hidrográficas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
        return []

# class ActionGeoConsulta(Action):

#     def name(self) -> Text:
#         return "action_geoconsulta"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
#         eje_pertenece = geo.funDinamicQuerry(tracker.latest_message['intent'], tracker.latest_message.get('place'))
#         dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
        
#         return []

########-------------------------------------------------ORDEN ALFABETICO-----------------------------------------------------------------------------
#Action accidentes_de_transito_siniestros
class Action_accidentes_de_transito_siniestros(Action):

	def name(self) -> Text:
		return "action_accidentes_de_transito_siniestros"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("accidentes_de_transito_siniestros")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [accidentes_de_tránsito_siniestros](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action actividades_economicas
class Action_actividades_economicas(Action):

	def name(self) -> Text:
		return "action_actividades_economicas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("actividades_economicas")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [actividades_económicas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []


#Action adjudicaciones_de_agua
class Action_adjudicaciones_de_agua(Action):

	def name(self) -> Text:
		return "action_adjudicaciones_de_agua"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("adjudicaciones_de_agua")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [adjudicaciones_de_agua](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action adultos_mayores
class Action_adultos_mayores(Action):

	def name(self) -> Text:
		return "action_adultos_mayores"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("adultos_mayores")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [adultos_mayores](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []


#Action adultos_mayores_discapacidad
class Action_adultos_mayores_discapacidad(Action):

	def name(self) -> Text:
		return "action_adultos_mayores_discapacidad"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("adultos_mayores_discapacidad")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [personas_con_discapacidad](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action alcantarillado
class Action_alcantarillado(Action):

	def name(self) -> Text:
		return "action_alcantarillado"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("alcantarillado")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [alcantarillado](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action areas_historicas
class Action_areas_historicas(Action):

	def name(self) -> Text:
		return "action_areas_historicas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("areas_historicas")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [áreas_históricas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action areas_protegidas
class Action_areas_protegidas(Action):

	def name(self) -> Text:
		return "action_areas_protegidas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("areas_protegidas")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [áreas_protegidas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action areas_verdes
class Action_areas_verdes(Action):

	def name(self) -> Text:
		return "action_areas_verdes"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("areas_verdes")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [áreas_verdes](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action areas_verdes_arboles
class Action_areas_verdes_arboles(Action):

	def name(self) -> Text:
		return "action_areas_verdes_arboles"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("areas_verdes_arboles")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [áreas_verdes_árboles](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action areas_verdes_parque_cajas
class Action_areas_verdes_parque_cajas(Action):

	def name(self) -> Text:
		return "action_areas_verdes_parque_cajas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("cajas")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [Parque_Nacional_Cajas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action areas_verdes_parques
class Action_areas_verdes_parques(Action):

	def name(self) -> Text:
		return "action_parques"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("parques")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [áreas_verdes_parques](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action asentamientos_humanos
class Action_asentamientos_humanos(Action):

	def name(self) -> Text:
		return "action_asentamientos_humanos"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("asentamientos_humanos")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [asentamientos_humanos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action biosfera
class Action_biosfera(Action):

	def name(self) -> Text:
		return "action_biosfera"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("biosfera")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [biósfera](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	
#Action cabecera_cantonal
class Action_cabecera_cantonal(Action):

	def name(self) -> Text:
		return "action_cabecera_cantonal"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("cabecera_cantonal")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [cabecera_cantonal](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action calidad_del_aire
class Action_calidad_del_aire(Action):

	def name(self) -> Text:
		return "action_calidad_del_aire"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("calidad_del_aire")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [calidad_del_aire](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action canalizacion
class Action_canalizacion(Action):

	def name(self) -> Text:
		return "action_canalizacion"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("canalizacion")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [canalización](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action cantones_del_azual
class Action_cantones_del_azual(Action):

	def name(self) -> Text:
		return "action_cantones_del_azual"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("cantones_del_azual")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [cantones_del_azual](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	
#Action cartografia
class Action_cartografia(Action):

	def name(self) -> Text:
		return "action_cartografia"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("cartografia")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [cartografia](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	
#Action catastro
class Action_catastro(Action):

	def name(self) -> Text:
		return "action_catastro"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("catastro")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [catastro](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action circuito
class Action_circuito(Action):

	def name(self) -> Text:
		return "action_circuito"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("circuito")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [circuito](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action clima
class Action_clima(Action):

	def name(self) -> Text:
		return "action_clima"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("clima")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [clima](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action clima_fenomeno_del_niño
class Action_clima_fenomeno_del_nino(Action):

	def name(self) -> Text:
		return "action_clima_fenomeno_del_nino"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("clima_fenomeno_del_niño")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [clima_fenómeno_del_niño](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action clima_lluvia
class Action_clima_lluvia(Action):

	def name(self) -> Text:
		return "action_lluvia"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("clima_lluvia")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [clima_lluvia](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action cobertura_vegetal
class Action_cobertura_vegetal(Action):

	def name(self) -> Text:
		return "action_cobertura_vegetal"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("cobertura_vegetal")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [cobertura_vegetal](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action cuencas_hidrograficas
class Action_cuencas_hidrograficas(Action):

	def name(self) -> Text:
		return "action_cuencas_hidrograficas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("cuencas_hidrográficas")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [cuencas_hidrograficas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action distritos
class Action_distritos(Action):

	def name(self) -> Text:
		return "action_distritos"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("distritos")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [distritos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action ductos
class Action_ductos(Action):

	def name(self) -> Text:
		return "action_ductos"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("ductos")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [ductos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action energia_electrica
class Action_energia_electrica(Action):

	def name(self) -> Text:
		return "action_energia_electrica"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("energia_electrica")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [energía_electrica](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []


#Action equipamiento_aprovisionamiento
class Action_equipamiento_aprovisionamiento(Action):

	def name(self) -> Text:
		return "action_equipamiento_aprovisionamiento"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("equipamiento_aprovisionamiento")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [equipamiento_aprovisionamiento](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action equipamiento_bienestar_social
class Action_equipamiento_bienestar_social(Action):

	def name(self) -> Text:
		return "action_equipamiento_bienestar_social"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("equipamiento_bienestar_social")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [equipamiento_bienestar_social](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	
#Action equipamiento_educacion
class Action_equipamiento_educacion(Action):

	def name(self) -> Text:
		return "action_equipamiento_educacion"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("equipamiento_educacion")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [equipamiento_educación](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	

#Action equipamiento_recoleccion
class Action_equipamiento_recoleccion(Action):

	def name(self) -> Text:
		return "action_equipamiento_recoleccion"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("equipamiento_recoleccion")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [equipamiento_recolección](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	

#Action equipamiento_recreacion_y_deporte
class Action_equipamiento_recreacion_y_deporte(Action):

	def name(self) -> Text:
		return "action_equipamiento_recreacion_y_deporte"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("equipamiento_recreacion_y_deporte")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [equipamiento_recreación_y_deporte](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action equipamiento_salud
class Action_equipamiento_salud(Action):

	def name(self) -> Text:
		return "action_equipamiento_salud"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("equipamiento_salud")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [equipamiento_salud](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action equipamiento_seguridad
class Action_equipamiento_seguridad(Action):

	def name(self) -> Text:
		return "action_equipamiento_seguridad"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("equipamiento_seguridad")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [equipamiento_seguridad](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	
#Action equipamiento_servicio
class Action_equipamiento_servicio(Action):

	def name(self) -> Text:
		return "action_equipamiento_servicio"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("equipamiento_servicio")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [equipamiento_servicio](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action erosion_de_suelos
class Action_erosion_de_suelos(Action):

	def name(self) -> Text:
		return "action_erosion_de_suelos"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("erosion_de_suelos")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [erosión_de_suelos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action estaciones
class Action_estaciones(Action):

	def name(self) -> Text:
		return "action_estaciones"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("estaciones")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [estaciones](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action etapa
class Action_etapa(Action):

	def name(self) -> Text:
		return "action_etapa"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("etapa")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [etapa](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action explotacion_minera
class Action_explotacion_minera(Action):

	def name(self) -> Text:
		return "action_explotacion_minera"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("explotacion_minera")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [explotación_minera](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action gas
class Action_gas(Action):

	def name(self) -> Text:
		return "action_gas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("gas")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [gas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action gasolineras
class Action_gasolineras(Action):

	def name(self) -> Text:
		return "action_gasolineras"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("gasolineras")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [gasolineras](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	
#Action geologia
class Action_geologia(Action):

	def name(self) -> Text:
		return "action_geologia"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("geologia")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [geología](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []


#Action geopedologia
class Action_geopedologia(Action):

	def name(self) -> Text:
		return "action_geopedologia"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("geopedologia")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [geopedología](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action humedales
class Action_humedales(Action):

	def name(self) -> Text:
		return "action_humedales"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("humedales")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [humedales](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action imagen_satelital
class Action_imagen_satelital(Action):

	def name(self) -> Text:
		return "action_imagen_satelital"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("imagen_satelital")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [imagen_satelital](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action incendios_
class Action_incendios_(Action):

	def name(self) -> Text:
		return "action_incendios"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("incendios")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [incendios_](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action indice_de_envegecimiento
class Action_indice_de_envegecimiento(Action):

	def name(self) -> Text:
		return "action_indice_de_envegecimiento"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("indice_de_envegecimiento")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [índice_de_envegecimiento](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action industria_pequeña
class Action_industria_pequeña(Action):

	def name(self) -> Text:
		return "action_industria_pequeña"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("industria_pequeña")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [industria_pequeña](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action infrestructura_transporte
class Action_infrestructura_transporte(Action):

	def name(self) -> Text:
		return "action_infrestructura_transporte"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("infrestructura_transporte")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [infrestructura_transporte](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action infrestructura_vial
class Action_infrestructura_vial(Action):

	def name(self) -> Text:
		return "action_infrestructura_vial"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("infrestructura_vial")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [infrestructura_vial](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action inpecciones_de_riesgos
class Action_inpecciones_de_riesgos(Action):

	def name(self) -> Text:
		return "action_inspecciones_de_riesgos"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("inpecciones_de_riesgos")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [inspecciones_de_riesgos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action internet
class Action_internet(Action):

	def name(self) -> Text:
		return "action_internet"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("internet")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [internet](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action jerarquia_de_asentamientos
class Action_jerarquia_de_asentamientos(Action):

	def name(self) -> Text:
		return "action_jerarquia_de_asentamientos"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("jerarquia_de_asentamientos")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [jerarquía_de_asentamientos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []


#Action limites
class Action_limites(Action):

	def name(self) -> Text:
		return "action_limites"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("limites")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [límites](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action manzanas
class Action_manzanas(Action):

	def name(self) -> Text:
		return "action_manzanas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("manzanas")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [manzanas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action montañas_y_lomas
class Action_montañas_y_lomas(Action):

	def name(self) -> Text:
		return "action_montañas_y_lomas"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("montañas_y_lomas")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [montañas_y_lomas](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action parroquias
class Action_parroquias(Action):

	def name(self) -> Text:
		return "action_parroquias"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("parroquias")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [parroquias](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action parroquias
class Action_parroquias(Action):

	def name(self) -> Text:
		return "action_predios"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("predios")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [predios_urbanos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	
    #Action riesgo_de_deslizamientos
class Action_riesgo_de_deslizamientos(Action):

	def name(self) -> Text:
		return "action_riesgo_de_deslizamientos"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("riesgo_de_deslizamientos")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [riesgo_de_deslizamientos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action riesgos_de_caida
class Action_riesgos_de_caida(Action):

	def name(self) -> Text:
		return "action_riesgos_de_caida"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("riesgos_de_caida")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [riesgos_de_caida](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action relieve
class Action_relieve(Action):

	def name(self) -> Text:
		return "action_relieve"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("relieves")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [relieves](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action tipos_de_suelos
class Action_tipos_de_suelos(Action):

	def name(self) -> Text:
		return "action_tipos_de_suelos"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("tipos_de_suelos")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [tipos_de_suelos](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []

#Action zona_agricola
class Action_zona_agricola(Action):

	def name(self) -> Text:
		return "action_zona_agricola"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("zona_agricola")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [zona_agrícola](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
		return []
	
#Action zona_industrial
class Action_zona_industrial(Action):

	def name(self) -> Text:
		return "action_zona_industrial"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

		eje_pertenece = geo.funDinamicQuerry("zona_industrial")
		dispatcher.utter_message(response="utter_cargando_visor", eje= eje_pertenece)
		dispatcher.utter_message(text="Clic aquí para ver resultado: [zona_industrial](https://ide.ucuenca.edu.ec/geoportal/viwer/100)")
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

